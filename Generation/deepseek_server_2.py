from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

app = Flask(__name__)

print("\U0001F680 Loading DeepSeek-Coder-Instruct model...")
model_name = "deepseek-ai/deepseek-coder-1.3b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print("✅ DeepSeek-Coder-Instruct model loaded on", device)

def split_diffs_by_file(diff_text: str) -> dict:
    print("🔍 Splitting diff into individual files...")
    files = {}
    current_file = None
    current_diff = []

    for line in diff_text.splitlines():
        if line.startswith('--- '):
            # Save previous file's diff if it exists
            if current_file and current_diff:
                files[current_file] = "\n".join(current_diff)
                current_diff = []

            # Extract filename from '--- ./filename'
            path = line.split()[1]
            current_file = path.lstrip("./")  # Remove './' prefix if present
            current_diff = [line]
        elif current_diff is not None:
            current_diff.append(line)

    # Save the last file's diff
    if current_file and current_diff:
        files[current_file] = "\n".join(current_diff)

    print(f"📂 Found diffs for {len(files)} files.")
    return files

# ORIGINAL VERSION FOR REFERENCE:
# def split_diffs_by_file(diff_text: str) -> dict:
#     print("🔍 Splitting diff into individual files...")
#     files = {}
#     current_file = None
#     current_diff = []
#
#     for line in diff_text.splitlines():
#         if line.startswith("diff --git"):
#             if current_file and current_diff:
#                 files[current_file] = "\n".join(current_diff)
#             parts = line.split(" ")
#             if len(parts) >= 4:
#                 current_file = parts[2][2:]  # strip 'a/' prefix
#                 current_diff = [line]
#         elif current_file:
#             current_diff.append(line)
#
#     if current_file and current_diff:
#         files[current_file] = "\n".join(current_diff)
#
#     print(f"📂 Found diffs for {len(files)} files.")
#     return files


def clean_diff(diff: str) -> str:
    """
    Annotate diff lines as [ADDED] or [REMOVED] for clearer model guidance.
    Strips hunk metadata and keeps only meaningful changes.
    """
    lines = []
    for line in diff.splitlines():
        if line.startswith("@@"):
            continue
        if line.startswith("+") and not line.startswith("+++"):
            lines.append("[ADDED] " + line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            lines.append("[REMOVED] " + line[1:].strip())
    return "\n".join(lines)



def generate_commit_message_for_file(diff: str, filename: str) -> str:
    print(f"✏️ Generating commit message for: {filename} (diff length: {len(diff)} chars)")
    cleaned_diff = clean_diff(diff)
    print(f'cleaned_diff: {clean_diff}')
    # prompt = (
    #     "You are a Git commit message generator. "
    #     "Respond only with a one-line Git commit message in imperative mood. "
    #     "Do not include explanations, prefixes, or formatting. "
    #     "All lines below are changes — either additions or removals. "
    #     "Each line starts with [ADDED] or [REMOVED]. Summarize what was added or removed accordingly.\n\n"
    #     f"{cleaned_diff}\n"
    #     "Commit message:"
    # )
    prompt = (
        "### SYSTEM INSTRUCTION ###\n"
        "Below is a list of ONLY added and removed lines. There are NO unchanged lines.\n"
        "Each line is prefixed with either [ADDED] or [REMOVED].\n\n"
        "Generate a one-line Git commit message describing what functionality was added or removed.\n"
        "Ignore functions or print statements that are still present in the file — focus ONLY on the removed or added lines.\n\n"
        f"{cleaned_diff}\n"
        "Commit message:"
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(device)
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
    message = decoded.split("Commit message:")[-1].strip().splitlines()[0]

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
