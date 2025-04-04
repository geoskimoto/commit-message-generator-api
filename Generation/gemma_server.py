# Gemma server for generating commit messages from diffs
# You need to open gemma on huggingface and accept terms to use it
# Edit api key setting on huggingface.co to allow access to staged models (check the boxes)

# This model is very slow and requires a lot of memory



from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import uvicorn
import logging

# --- Config ---
MODEL_NAME = "google/gemma-1.1-2b-it"
HF_AUTH_TOKEN = "Token goes here"  # Replace this

# --- Logging setup ---
logging.basicConfig(level=logging.INFO)

# --- Load model/tokenizer ---
print(f"🔄 Loading model: {MODEL_NAME}")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    token=HF_AUTH_TOKEN,
    trust_remote_code=True
)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    token=HF_AUTH_TOKEN,
    trust_remote_code=True,
    torch_dtype=torch.float32,
    device_map="cpu"
)

# --- FastAPI setup ---
app = FastAPI()

class DiffRequest(BaseModel):
    diff: str

@app.post("/generate")
async def generate_commit_message(req: DiffRequest):
    print("\n✅ Received POST /generate")

    diff = req.diff.strip()
    print(f"📝 Input diff:\n{diff[:1000]}")  # print at most 1000 chars

    prompt = (
        "Write a Git commit message for this change:\n\n"
        f"Git diff:\n{diff}\n\n"
        "Commit message:"
    )
    print(f"\n📥 Prompt:\n{prompt[:1000]}")

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    print(f"\n🔢 Tokenized input IDs:\n{inputs['input_ids'][0].tolist()}")

    # output = model.generate(
    #     **inputs,
    #     max_new_tokens=50,
    #     do_sample=True,
    #     temperature=0.7,
    #     top_k=50,
    #     top_p=0.95,
    #     eos_token_id=tokenizer.eos_token_id
    # )
    output = model.generate(
        **inputs,
        max_new_tokens=20,  # was 50
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95,
        eos_token_id=tokenizer.eos_token_id
    )

    print(f"\n📤 Output token IDs:\n{output[0].tolist()}")

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)
    print(f"\n🧾 Full decoded output:\n{decoded}")

    # Extract just the commit message
    if "Commit message:" in decoded:
        commit_message = decoded.split("Commit message:")[-1].strip()
    else:
        commit_message = decoded.strip()

    print(f"\n✅ Final Commit Message:\n{commit_message}\n")

    return {"commit_message": commit_message}

# --- Run server on port 8000 ---
if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
