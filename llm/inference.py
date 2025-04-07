from .model_loader import load_model
import torch

model, tokenizer = load_model()

def generate_response(prompt: str, max_tokens: int = 256) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.7,
            do_sample=True,
            top_p=0.95
        )
    return tokenizer.decode(output[0], skip_special_tokens=True)