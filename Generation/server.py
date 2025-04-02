import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
# from model import CodeT5
api_key = os.getenv("hugging_face_api_key")

app = FastAPI()

# Load model
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

class DiffRequest(BaseModel):
    diff: str

@app.post("/generate")
def generate_commit_message(request: DiffRequest):
    prompt = f"Generate commit message: {request.diff}"
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    
    output = model.generate(**inputs, max_length=50)
    commit_message = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return {"commit_message": commit_message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
