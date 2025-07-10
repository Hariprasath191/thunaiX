from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load local GPT-2 model
model_name = "distilgpt2"  # Or "gpt2" for bigger model
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model.eval()

# FastAPI app
app = FastAPI()

# Allow frontend to call this backend
origins = [
    "http://localhost:4200",  # Angular dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request & Response models
class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    reply: str

# Local GPT-2 generate function
def generate_text(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Chat endpoint
@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    reply = generate_text(request.prompt)
    return ChatResponse(reply=reply)
