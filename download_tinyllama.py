# Script to complete tinyLlama download
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0" # hold model version

print("Tokenizer: ")
tokenizer = AutoTokenizer.from_pretrained(model_id)

print("Model download")     
model = AutoModelForCausalLM.from_pretrained(model_id)

print("Downloaded succesfully")
