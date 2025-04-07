from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "tinyllama")

def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForCausalLM.from_pretrained(MODEL_DIR).to(device)
    model.eval()
    return model, tokenizer