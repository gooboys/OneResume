from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0"
SAVE_DIR = "tinyllama"

print("Downloading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
tokenizer.save_pretrained(SAVE_DIR)

print("Downloading model...")
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
model.save_pretrained(SAVE_DIR)

print(f"✅ Model downloaded to: ./{SAVE_DIR}")