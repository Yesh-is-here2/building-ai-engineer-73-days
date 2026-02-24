# Building an AI Engineer in 73 Days

A structured end-to-end AI Engineering program covering:

- Machine Learning Foundations
- LLM Engineering
- AI APIs
- Full Stack Systems
- Data Systems
- Reproducibility
- Production Practices

This repository documents **73 days of AI engineering development** with proof artifacts for every module.

The goal was to build **real engineering skills**, not just tutorials.

---

# Project Structure
building-ai-engineer-73-days/

phase1_foundations/
Core ML + Git + Python fundamentals

phase2_llm_nlp/
16_transformers_tokenize
17_openai_completion
18_llama_local_stub
19_sentence_embeddings
20_faiss_similarity_search
21_chromadb_store_retrieve
22_pinecone_cloud_query
23_langchain_basic_chain
24_llamaindex_doc_qa
25_langgraph_workflow
26_spacy_noun_extraction
27_nltk_token_cleanup
28_prompt_comparison
29_safety_filter
30_llm_cli_chatbot

phase3_software_ai/
31_flask_basic_app
32_fastapi_hello
40_frontend_calls_api
41_basic_auth_token
42_env_token
43_ui_calls_protected_api
44_swagger_docs
45_ai_powered_api

phase5_data_systems_polish/
69_research_repro
72_portfolio_index
73_final_polish


---

# Core Skills Demonstrated

## AI Engineering

- Transformers tokenization
- Sentence embeddings
- Vector search
- Retrieval pipelines
- Prompt engineering
- Safety filtering
- CLI chatbots

### Tools

- Transformers
- SentenceTransformers
- FAISS
- ChromaDB
- Pinecone
- LangChain
- LlamaIndex
- PyTorch

---

# Backend Engineering

Built multiple production-style APIs.

## Flask API

### Endpoints


GET /
GET /health


### Features

- JSON responses
- Local server testing
- Log artifacts

---

## Express APIs

Built multiple services:


GET /health
POST /echo
POST /ai
GET /me


### Features

- JSON parsing
- REST design
- Token authentication
- Environment variables
- Swagger documentation

---

# Authentication Systems

Implemented **Bearer Token Authentication**

### Example


Authorization: Bearer devtoken123


### Learned

- Header parsing
- Token validation
- Middleware logic

---

# Frontend Integration

Built React frontends calling APIs.

### Flow


React UI
↓
Fetch API
↓
Express Backend
↓
JSON Response
↓
UI Display


### Technologies

- React
- Vite
- Fetch API

---

# AI API Design

Implemented AI endpoint.

### Endpoint


POST /ai


### Input


{
"user":"yesh",
"prompt":"Explain embeddings"
}


### Output


{
"ok": true,
"answer": "stub response"
}


### Architecture


Client
↓
API
↓
AI Logic
↓
JSON Response


---

# Data Engineering & Reproducibility

## Reproducible ML Experiment

### Module


69_research_repro


### Features

- Deterministic random seeds
- Metric logging
- Artifact saving
- Automated tests

### Artifacts


repro_metrics.json
main_output.txt


### Testing


pytest


---

# Portfolio Automation

## Automatic Index Generator

### Script


make_index.py


### Features

- Scans all modules
- Generates HTML index
- Creates GitHub links

### Output


index.html


---

# Artifact-Based Engineering

Each module contains proof artifacts:


output.txt
logs/
metrics/
files/


This ensures:

- Reproducibility
- Traceability
- Interview proof

---

# Major Engineering Challenges Solved

## Git Large File Disaster

### Problem

GitHub rejected push due to large files:


GH001: Large files detected


### Cause


.venv committed


### Solution


py -m git_filter_repo --force --path .venv --invert-paths
git gc --prune=now --aggressive
git push --force


### Result

Clean repository history.

---

## Repository Root Mistake

### Problem

Git root was accidentally:


C:\Users\akula


### Solution

Moved repository to:


Desktop/building-ai-engineer-73-days


---

## API Debugging

### Problems Solved

- Port conflicts
- JSON parsing errors
- curl vs PowerShell issues
- Missing dependencies

---

# Technologies Used

## Languages

- Python
- JavaScript

---

## AI/ML

- Transformers
- SentenceTransformers
- PyTorch
- FAISS
- ChromaDB
- Pinecone
- LangChain
- LlamaIndex

---

## Backend

- Flask
- FastAPI
- Express

---

## Frontend

- React
- Vite

---

## Tools

- Git
- GitHub
- PowerShell
- VSCode

---

## Testing

- Pytest

---

# Engineering Practices

This project emphasizes real engineering practices:

- Version control discipline
- Artifact logging
- Deterministic experiments
- API documentation
- Authentication
- Testing
- Modular design

---

# What This Project Demonstrates

This repository demonstrates ability to:

- Build AI systems end-to-end
- Design APIs
- Integrate AI into software
- Debug real problems
- Build reproducible pipelines
- Document engineering work

---

# Difficulty Level

## Overall Level

**Intermediate → Advanced**

### Includes

- LLM Engineering
- Backend Systems
- Full Stack Integration
- Reproducible ML
- Production Practices
