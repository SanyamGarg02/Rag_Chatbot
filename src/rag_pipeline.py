from src.retriever import retrieve_docs
from src.generator import generate_answer

def get_answer(query):
    retrieved_chunks = retrieve_docs(query)
    context = "\n\n".join(retrieved_chunks[:2])
    return generate_answer(context, query), retrieved_chunks
