import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load DistilGPT-2 model and tokenizer
model_name = "distilgpt2"  # Or "gpt2" for the base GPT-2 model
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set model to evaluation mode (no training)
model.eval()

# Generate Text Function
def generate_text(prompt, max_length=50):
    # Tokenize the input prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    # Generate text from the model
    with torch.no_grad():  # Turn off gradient calculation for inference
        outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    
    # Decode the generated output back to text
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Test the function
prompt = "Artificial intelligence is"
generated_text = generate_text(prompt)
print(generated_text)
