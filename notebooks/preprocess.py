from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
import os

# Load the document
loader = PyPDFLoader("data/user_agreement.pdf")
docs = loader.load()

# Chunk the text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# Create embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(chunks, embedding_model)

# Saving vector DB and chunks
os.makedirs("chunks", exist_ok=True)
os.makedirs("vectordb", exist_ok=True)
vectorstore.save_local("vectordb")

#saving raw chunks
with open("chunks/chunked_docs.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"\n--- Chunk {i+1} ---\n{chunk.page_content}\n")