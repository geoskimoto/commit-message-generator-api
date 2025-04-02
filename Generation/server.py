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


# test_input = tokenizer("Summarize: Added a new function", return_tensors="pt")
# test_output = model.generate(**test_input, max_length=50)
# test_message = tokenizer.decode(test_output[0], skip_special_tokens=True)
# print("Test Message:", test_message)



class DiffRequest(BaseModel):
    diff: str

@app.post("/generate")
def generate_commit_message(request: DiffRequest):
    print('Starting generate...')
    prompt = f"Summarize this code change into a commit message: {request.diff}"
    print("Prompt:", prompt)  # Debugging

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    print("Tokenized Inputs:", inputs)  # Debugging

    output = model.generate(**inputs, max_length=50)
    print("Raw Output:", output)  # Debugging

    commit_message = tokenizer.decode(output[0], skip_special_tokens=True)
    print("Generated Commit Message:", commit_message)  # Debugging

    return {"commit_message": commit_message}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
