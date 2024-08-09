import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Set model and tokenizer paths
model_path = "/home/lab730/Desktop/llama3-8b-lora-finetuned"
base_tokenizer_path = "meta-llama/Meta-Llama-3-8B"  

# Try loading the base model's tokenizer
try:
	tokenizer = AutoTokenizer.from_pretrained(base_tokenizer_path)
	print("The tokenizer of the base model is loaded successfully")
except Exception as e:
	print(f"Error loading tokenizer for base model: {e}")

# Load the model
try:
	model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float32)
	print("Successfully loaded the fine-tuned model")
except Exception as e:
	print(f"Error loading fine-tuned model: {e}")

# Create a text generation pipeline, force the use of CPU, and use GPU if there is enough memory
try:
	device = -1  # Force CPU usage
	generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device, batch_size=1)
	print("Successfully created a text generation pipeline")
except Exception as e:
	print(f"Error creating text generation pipeline: {e}")

# Input text
input_text = "Once upon a time, in a land far, far away, there was a"

# Generate text and adjust generation parameters
try:
	generated_texts = generator(input_text, max_length=100, num_return_sequences=1, num_beams=5, do_sample=True, temperature=0.7, top_p=0.9)
	# Print the generated text
	for i, generated_text in enumerate(generated_texts):
    	print(f"Generated Text {i + 1}: {generated_text['generated_text']}")
except Exception as e:
	print(f"Error generating text: {e}")
