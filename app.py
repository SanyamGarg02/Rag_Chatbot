import streamlit as st
from src.rag_pipeline import get_answer

st.set_page_config(page_title="Legal RAG Chatbot", layout="wide")
st.title("📜 Legal RAG Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.text_input("Ask a legal question based on the document:")

if query:
    with st.spinner("Generating..."):
        answer, sources = get_answer(query)
        st.session_state.chat.append((query, answer, sources))

for q, a, s in reversed(st.session_state.chat):
    st.markdown(f"**User:** {q}")
    st.markdown(f"**Bot:** {a}")
    with st.expander("See Sources"):
        for i, chunk in enumerate(s):
            st.text(f"Source {i+1}:\n{chunk}")

if st.button("Reset Chat"):
    st.session_state.chat = []