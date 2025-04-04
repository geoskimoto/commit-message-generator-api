import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

from datasets import load_dataset, load_from_disk, DatasetDict
from transformers import (
    T5Tokenizer, T5ForConditionalGeneration,
    TrainingArguments, Trainer
)
import os

USE_SAVED = os.path.exists("../tokenized_commitbench")

# Load model & tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

if USE_SAVED:
    print("📦 Loading previously tokenized dataset...")
    tokenized_datasets = load_from_disk("../tokenized_commitbench")
else:
    print("📥 Loading and preprocessing CommitBench dataset...")

    dataset = load_dataset("Maxscha/commitbench")

    # Subset for faster training (~30 min)
    dataset["train"] = dataset["train"].select(range(20000))
    dataset["validation"] = dataset["validation"].select(range(2000))

    def preprocess_function(examples):
        inputs = examples["diff"]
        targets = examples["message"]
        model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
        labels = tokenizer(targets, max_length=64, truncation=True, padding="max_length")
        model_inputs["labels"] = labels["input_ids"]
        return model_inputs

    tokenized_datasets = dataset.map(preprocess_function, batched=True)
    tokenized_datasets.save_to_disk("tokenized_commitbench")

# Training configuration
training_args = TrainingArguments(
    output_dir="t5-commit-gen",
    evaluation_strategy="epoch",
    logging_strategy="steps",
    logging_steps=100,
    save_total_limit=1,
    num_train_epochs=1,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=5e-5,
    weight_decay=0.01,
    report_to="none",  # Change to "wandb" or "tensorboard" if needed
    disable_tqdm=False,
    push_to_hub=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    tokenizer=tokenizer,
)

print("🚀 Starting training...")
trainer.train()

print("💾 Saving model...")
model.save_pretrained("./t5-commit-gen")
tokenizer.save_pretrained("./t5-commit-gen")
