from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("vectordb", embedding_model, allow_dangerous_deserialization=True)

def retrieve_docs(query, k=4):
    docs = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in docs]