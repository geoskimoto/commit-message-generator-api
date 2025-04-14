from flask import Flask, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = Flask(__name__)

# Load the fine-tuned model and tokenizer
MODEL_PATH = "./t5-commit-gen" # Path to the fine-tuned model
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


@app.route('/generate', methods=['POST'])
def generate_commit_message():
    try:
        data = request.get_json()
        if not data or "diff" not in data:
            return jsonify({"error": "Missing 'diff' in request body"}), 400

        diff_text = data["diff"]
        input_ids = tokenizer.encode(
            diff_text, return_tensors="pt", max_length=1024, truncation=True
        ).to(device)

        # outputs = model.generate(
        #     input_ids,
        #     max_length=64,
        #     num_beams=4,
        #     early_stopping=True,
        #     no_repeat_ngram_size=2
        # )

        outputs = model.generate(
            input_ids,
            num_beams=5,
            no_repeat_ngram_size=3,
            length_penalty=1.2,
            early_stopping=True
        )

        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return jsonify({"commit_message": decoded})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
