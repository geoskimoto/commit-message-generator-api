from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import torch
import time

app = Flask(__name__)

print("🚀 Loading microsoft/phi-1_5 model...")
model_name = "microsoft/phi-1_5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print("✅ Model loaded on", device)


# ORIGINAL VERSION FOR REFERENCE:
def split_diffs_by_file(diff_text: str) -> dict:
    print("🔍 Splitting diff into individual files...")
    files = {}
    current_file = None
    current_diff = []

    for line in diff_text.splitlines():
        if line.startswith("diff --git"):
            if current_file and current_diff:
                files[current_file] = "\n".join(current_diff)
            parts = line.split(" ")
            if len(parts) >= 4:
                current_file = parts[2][2:]  # strip 'a/' prefix
                current_diff = [line]
        elif current_file:
            current_diff.append(line)

    if current_file and current_diff:
        files[current_file] = "\n".join(current_diff)

    print(f"📂 Found diffs for {len(files)} files.")
    return files


def clean_diff(diff: str) -> str:
    """
    Clean the diff by keeping only meaningful lines (no metadata).
    Keep + and - prefixes to indicate changes.
    """
    lines = []
    for line in diff.splitlines():
        if line.startswith("@@") or line.startswith("+++ ") or line.startswith("--- "):
            continue
        if line.startswith("+") or line.startswith("-"):
            lines.append(line)
    return "\n".join(lines)


def generate_commit_message_for_file(diff: str, filename: str) -> str:
    print(f"✏️ Generating commit message for: {filename} (diff length: {len(diff)} chars)")
    cleaned_diff = clean_diff(diff)

    prompt = (
        "Below is a code diff and its corresponding commit message.\n"
        "Example:\n"
        "Diff:\n"
        "-# Get user info\n"
        "+# Retrieve user profile information\n"
        "Commit message:\nUpdate user info comment for clarity\n\n"
        "Diff:\n"
        f"{cleaned_diff}\n"
        "Commit message:\n"
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    start_time = time.time()
    outputs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=32,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id
    )
    end_time = time.time()

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    lines = decoded.split("Commit message:\n")
    message = lines[-1].strip().splitlines()[0] if len(lines) > 1 else decoded.splitlines()[0]

    print(f"⏱️ Generation for {filename} took {round(end_time - start_time, 2)}s")
    print(f"✅ Commit message for {filename}: {message}")
    return message




@app.route("/generate", methods=["POST"])
def generate_commit_messages():
    try:
        start_total = time.time()
        data = request.get_json()
        print(f'DATA: {data}')
        if not data or "diff" not in data:
            return jsonify({"error": "Missing 'diff' in request"}), 400

        raw_diff = data["diff"]
        file_diffs = split_diffs_by_file(raw_diff)

        message_lines = []
        for filename, diff in file_diffs.items():
            if diff.strip():
                message = generate_commit_message_for_file(diff, filename)
                message_lines.append(f"{filename}: {message}")
            else:
                print(f"⚠️ Skipping empty or uninformative diff for {filename}")

        final_message = "\n".join(message_lines)
        end_total = time.time()
        print(f"✅ Finished all generation in {round(end_total - start_total, 2)}s")
        print("📦 Final commit message:\n" + final_message)
        return jsonify({"commit_message": final_message})

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🌐 Starting Flask server on http://localhost:8000")
    app.run(host="localhost", port=8000)
