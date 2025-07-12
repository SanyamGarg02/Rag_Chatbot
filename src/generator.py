from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Load model + tokenizer
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

#pipeline
llm = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_answer(context, question):
    prompt = f"""Answer the following question using the provided context.

Context: {context}

Question: {question}"""
    
    result = llm(prompt, max_new_tokens=150, do_sample=False)[0]["generated_text"]
    return result.strip()