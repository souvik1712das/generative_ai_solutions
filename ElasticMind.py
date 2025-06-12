'''
author: Souvik Das
description: Local RAG Assistant using Streamlit, Elasticsearch, and Ollama.
version: 1.1
date: 2025-06-11

Steps
1. Open Command Prompt or PowerShell.
2. Activate your virtual environment (if not already active): .\.venv\Scripts\activate
3. Run the Streamlit app: streamlit run "c:/Users/souvik.das/OneDrive - Nihilent Limited/SelfStudy/POC - Local AI Agent with Python/AI Agent with Local LLM.py"
'''

import streamlit as st
import pandas as pd
import requests
import json
from elasticsearch import Elasticsearch

# --- Config ---
OLLAMA_HOST = "http://localhost:11434"
EMBED_MODEL = "mxbai-embed-large"
GEN_MODEL = "mistral"

# --- Connect to ES ---
es = Elasticsearch(
    "https://elastic:G==Q=Y7a=BDFzD_gVEcs@localhost:9200",
    ca_certs=False,
    verify_certs=False
)

# --- Embedding function ---
def get_embedding(text, model=EMBED_MODEL):
    url = f"{OLLAMA_HOST}/api/embeddings"
    headers = {"Content-Type": "application/json"}
    data = {"model": model, "prompt": text}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()["embedding"]

# --- Create index with mapping ---
def create_index(index_name):
    mapping = {
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "embedding": {
                    "type": "dense_vector",
                    "dims": 1024,
                    "index": True,
                    "similarity": "cosine"
                }
            }
        }
    }
    es.indices.create(index=index_name, body=mapping)

# --- Index a document ---
def index_doc(text, index_name):
    embedding = get_embedding(text)
    doc = {"text": text, "embedding": embedding}
    es.index(index=index_name, body=doc)

# --- Generate answer from model ---
def generate_answer_with_mistral(context, question):
    prompt = f"""Answer the question based on the context below.

Context:
{context}

Question:
{question}

Answer:"""
    data = {
        "model": GEN_MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )
    response.raise_for_status()
    return response.json()["response"]

# --- RAG Query ---
def rag_query(question, index_name):
    question_vector = get_embedding(question)
    query = {
        "size": 3,
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": question_vector}
                }
            }
        }
    }
    response = es.search(index=index_name, body=query)
    context = " ".join(hit["_source"]["text"] for hit in response["hits"]["hits"])
    return generate_answer_with_mistral(context, question)

# --- Streamlit UI ---
st.title("🧠 ElasticMind - Where Questions Meet Context — with RAG & Local LLMs")

# === Upload & Embed Section ===
st.header("📂 Upload & Embed File")
uploaded_file = st.file_uploader("Upload CSV or TXT", type=["csv", "txt"])
index_name_input = st.text_input("Enter index name for embedding", placeholder="e.g. fintech_logs")

if uploaded_file:
    if not index_name_input.strip():
        st.warning("Please enter a valid index name.")
    else:
        if es.indices.exists(index=index_name_input):
            use_existing = st.radio(
                f"Index '{index_name_input}' already exists. What would you like to do?",
                ("Use existing index", "Create new index with different name")
            )
            if use_existing == "Create new index with different name":
                index_name_input = st.text_input("Enter new index name", "")
        
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            st.write("Preview:", df.head())
            if st.button("Embed Data"):
                if not es.indices.exists(index=index_name_input):
                    create_index(index_name_input)
                for _, row in df.iterrows():
                    text = " | ".join(f"{col}: {row[col]}" for col in row.index)
                    index_doc(text, index_name_input)
                st.success("CSV data embedded to Elasticsearch.")
        elif uploaded_file.name.endswith(".txt"):
            text = uploaded_file.read().decode("utf-8")
            st.text_area("Preview", text[:1000])
            if st.button("Embed TXT Data"):
                if not es.indices.exists(index=index_name_input):
                    create_index(index_name_input)
                index_doc(text, index_name_input)
                st.success("Text data embedded to Elasticsearch.")

# === RAG Question-Answer Section ===
st.header("❓ Ask a Question Using RAG")

query_index_name = st.text_input("Index name to query", placeholder="e.g. fintech_logs")
question = st.text_input("Your question")

if st.button("Get Answer"):
    if not query_index_name.strip():
        st.warning("Please enter the index name to query.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = rag_query(question, query_index_name)
                st.success("Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error querying index: {e}")
