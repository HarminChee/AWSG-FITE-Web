from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, EvalPrediction
from transformers.trainer_utils import EvalLoopOutput
from peft import LoraConfig, PeftModel, get_peft_model
import torch
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace with your Hugging Face access token
token = "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"

# Load the model and tokenizer
try:
	logger.info("Loading the model and tokenizer")
	model_name = "meta-llama/Meta-Llama-3-8B"
	base_model = AutoModelForCausalLM.from_pretrained(
    	model_name,
    	token=token,
    	low_cpu_mem_usage=True,
    	torch_dtype=torch.float32,
    	device_map="auto"
	)

	tokenizer = AutoTokenizer.from_pretrained(
    	model_name,
    	token=token,
    	trust_remote_code=True
	)
	tokenizer.pad_token = tokenizer.eos_token
	tokenizer.padding_side = "right"
except Exception as e:
	logger.error(f"Error loading model and tokenizer: {e}")
	raise

# Load the IMDB dataset
try:
	logger.info("Loading the dataset")
	dataset = load_dataset("imdb", split='train[:1%]')
	eval_dataset = load_dataset("imdb", split='test[:1%]')
except Exception as e:
	logger.error(f"Error loading dataset: {e}")
	raise

# Configure LoRA
try:
	logger.info("Configuring LoRA")
	lora_config = LoraConfig(
    	r=16,
    	lora_alpha=32,
    	target_modules=["q_proj", "v_proj"],
    	lora_dropout=0.1,
    	bias="none"
	)

	model = get_peft_model(base_model, lora_config)
except Exception as e:
	logger.error(f"Error when configuring LoRA: {e}")
	raise

# Data preprocessing function
def preprocess_function(examples):
	try:
    	tokenized_inputs = tokenizer(examples['text'], truncation=True, padding='max_length', max_length=512)
    	tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()
    	return tokenized_inputs
	except Exception as e:
    	logger.error(f"Error in preprocessing data: {e}")
    	raise

try:
	logger.info("Preprocessing the dataset")
	tokenized_dataset = dataset.map(preprocess_function, batched=True)
	tokenized_eval_dataset = eval_dataset.map(preprocess_function, batched=True)
except Exception as e:
	logger.error(f"Error while preprocessing dataset: {e}")
	raise

# Set training parameters
training_args = TrainingArguments(
	output_dir="./llama3-8b-lora-finetuned",
	per_device_train_batch_size=1,
	gradient_accumulation_steps=2,
	num_train_epochs=3,
	logging_steps=10,
	save_steps=10,
	eval_strategy="steps",
	eval_steps=10,
	fp16=False,
	save_total_limit=2,
	load_best_model_at_end=True,
	metric_for_best_model="eval_loss"
)

# Customize Trainer to ensure loss value is returned
class CustomTrainer(Trainer):
	def compute_loss(self, model, inputs, return_outputs=False):
    	try:
        	labels = inputs.pop("labels")
        	outputs = model(**inputs)
        	logits = outputs.get("logits")
        	loss_fct = torch.nn.CrossEntropyLoss()
        	shift_logits = logits[..., :-1, :].contiguous()
        	shift_labels = labels[..., 1:].contiguous()
        	loss = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1))
        	return (loss, outputs) if return_outputs else loss
    	except Exception as e:
        	logger.error(f"Error calculating loss: {e}")
        	raise
    
	def prediction_step(self, model, inputs, prediction_loss_only, ignore_keys=None):
    	try:
        	has_labels = all(inputs.get(k) is not None for k in self.label_names)
        	inputs = self._prepare_inputs(inputs)
        	with torch.no_grad():
            	outputs = model(**inputs)
            	if has_labels:
                	loss = self.compute_loss(model, inputs).detach()
            	else:
                	loss = None

        	if prediction_loss_only:
            	return (loss, None, None)

        	logits = outputs.get("logits")

        	return (loss, logits, inputs.get("labels"))
    	except Exception as e:
        	logger.error(f"Error in prediction step: {e}")
        	raise
    
	def evaluate(self, eval_dataset=None, ignore_keys=None, metric_key_prefix="eval"):
    	try:
        	eval_dataloader = self.get_eval_dataloader(eval_dataset)
        	output = self.prediction_loop(
            	eval_dataloader,
            	description="Evaluation",
            	prediction_loss_only=True if self.compute_metrics is None else None,
            	ignore_keys=ignore_keys,
            	metric_key_prefix=metric_key_prefix,
        	)
        	metrics = output.metrics
        	# Make sure 'eval_loss' exists in the evaluation metrics
        	if "eval_loss" not in metrics:
            	metrics["eval_loss"] = output.predictions.mean().item() if isinstance(output.predictions, torch.Tensor) else output.predictions
        	self.log(metrics)
        	return metrics
    	except Exception as e:
        	logger.error(f"Error while evaluating: {e}")
        	raise
    
	def prediction_loop(self, dataloader, description, prediction_loss_only=None, ignore_keys=None, metric_key_prefix="eval"):
    	try:
        	model = self._wrap_model(self.model, training=False)
        	batch_size = dataloader.batch_size
        	if not isinstance(batch_size, int):
            	batch_size = 1

        	model.eval()

        	if self.args.past_index >= 0:
            	self._past = None

        	num_examples = self.num_examples(dataloader)
        	all_losses = []
        	all_preds = []
        	all_labels = []

        	for step, inputs in enumerate(dataloader):
            	loss, logits, labels = self.prediction_step(model, inputs, prediction_loss_only, ignore_keys=ignore_keys)

            	if loss is not None:
                	all_losses.append(loss.repeat(batch_size))

            	if logits is not None:
                	all_preds.append(logits)
            	if labels is not None:
                	all_labels.append(labels)

        	if all_losses:
            	all_losses = torch.cat(all_losses, dim=0)
        	else:
            	all_losses = torch.tensor([])

        	if all_preds:
            	all_preds = torch.cat(all_preds, dim=0)
        	else:
            	all_preds = torch.tensor([])

        	if all_labels:
            	all_labels = torch.cat(all_labels, dim=0)
        	else:
            	all_labels = torch.tensor([])

        	metrics = {metric_key_prefix + "_loss": all_losses.mean().item() if all_losses.size(0) > 0 else 0.0}

        	return EvalLoopOutput(predictions=all_preds, label_ids=all_labels, metrics=metrics, num_samples=num_examples)
    	except Exception as e:
        	logger.error(f"Error predicting loop: {e}")
        	raise

# Creating a custom Trainer
trainer = CustomTrainer(
	model=model,
	args=training_args,
	train_dataset=tokenized_dataset,
	eval_dataset=tokenized_eval_dataset
)

try:
	logger.info("Start training")
	trainer.train()
except Exception as e:
	logger.error(f"Error during training: {e}")
	raise

# Save the fine-tuned model
try:
	logger.info("Save the model")
	model.save_pretrained("./llama3-8b-lora-finetuned")
except Exception as e:
	logger.error(f"Error saving model: {e}")
	raise

