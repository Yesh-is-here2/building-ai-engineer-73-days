# Building an AI Engineer in 73 Days 🚀
### End-to-End AI Engineering Program — From Foundations to Production

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?style=for-the-badge&logo=pytorch)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black?style=for-the-badge&logo=openai)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?style=for-the-badge&logo=docker)
![MLflow](https://img.shields.io/badge/MLflow-Latest-0194E2?style=for-the-badge)

**73 consecutive days. 73 working AI engineering projects. Every day, something shipped.**

[Phases](#phases) · [Tech Stack](#tech-stack) · [Structure](#structure) · [Key Projects](#key-projects)

</div>

---

## What is This?

A structured, self-directed AI engineering program where I built and shipped **one complete, working project every single day for 73 consecutive days** — not tutorials, not walkthroughs, but real working code with output artifacts proving execution.

The goal: build real AI engineering skills across the full stack — from ML fundamentals and LLM engineering, to backend systems, MLOps, and data infrastructure.

**73 days. 73 modules. Every module has:**
- ✅ Working Python code
- 📄 Output artifacts (`output.txt`, `logs/`, `metrics/`)
- 📖 Documentation (`run.md`)
- 🧪 Tests where applicable (`pytest`)

---

## Learning Journey Overview

```
Day 1                    Day 15                   Day 30
  │                        │                        │
  ▼                        ▼                        ▼
Phase 1               Phase 2                  Phase 3
Core ML           LLM & NLP Eng.          Software AI
Foundations       ─────────────           Integration
                                               │
Day 45                   Day 60               │
  │                        │                  │
  ▼                        ▼                  ▼
Phase 4               Phase 5
MLOps & Cloud      Data Systems
                   & Polish
                                          Day 73
                                            │
                                            ▼
                                        Portfolio
                                        Complete ✓
```

---

## Phases

### Phase 1 — Core ML Foundations (Days 1–15)

```
Day 01  Python basics         — datetime, random, functions
Day 02  Bash scripting        — shell commands, file operations
Day 03  NumPy playground      — arrays, vectorized operations, math
Day 04  Pandas + CSV          — DataFrames, read_csv, head, shape
Day 05  SQL learning          — SELECT, JOIN, WHERE, GROUP BY
Day 06  PostgreSQL            — psycopg2, CREATE TABLE, INSERT
Day 07  Linear Regression     — scikit-learn fit/predict/coef
Day 08  XGBoost               — gradient boosted trees, DMatrix
Day 09  PyTorch tensors       — tensor ops, addition, multiplication
Day 10  TensorFlow Dense      — Sequential model, compile, fit
Day 11  Jupyter Notebook      — interactive ML environment
Day 12  Git fundamentals      — version control, commit, push
Day 13  Docker basics         — Dockerfile, build, run
Day 14  Docker Compose        — multi-container, database container
Day 15  End-to-end ML         — train_test_split, MAE evaluation
```

### Phase 2 — LLM & NLP Engineering (Days 16–30)

```
Day 16  HuggingFace Transformers — AutoTokenizer, BERT, token IDs
Day 17  OpenAI Completion        — gpt-4o-mini, Chat Completions API
Day 18  LLaMA Local Stub         — offline LLM pipeline pattern
Day 19  Sentence Embeddings      — all-MiniLM-L6-v2, cosine similarity
Day 20  FAISS Similarity Search  — IndexFlatL2, ANN, vector retrieval
Day 21  ChromaDB                 — collection, add, query, metadata
Day 22  Pinecone Cloud           — cloud vector DB, credential management
Day 23  LangChain Basic Chain    — PromptTemplate, LLMChain
Day 24  LlamaIndex Doc QA        — VectorStoreIndex, query engine
Day 25  LangGraph Workflow       — stateful graph, nodes, edges
Day 26  SpaCy NLP                — noun extraction, POS tagging
Day 27  NLTK                     — tokenization, stopwords, stemming
Day 28  Prompt Comparison        — zero-shot vs few-shot vs CoT
Day 29  Safety Filter            — content moderation before LLM call
Day 30  CLI Chatbot              — terminal LLM conversation loop
```

### Phase 3 — Software AI Integration (Days 31–45)

```
Day 31  Flask API               — GET /health, JSON responses
Day 32  FastAPI                 — async endpoints, auto Swagger docs
Day 33  REST POST endpoint      — request body, Pydantic validation
Day 34  gRPC unary demo         — .proto files, stub generation
Day 35  Redis cache             — SET/GET/TTL, latency measurement
Day 36  MongoDB                 — insert_one, find_one, documents
Day 37  Backend logic flow      — service layer architecture pattern
Day 38  React UI                — components, state management
Day 39  TypeScript              — types, interfaces, type safety
Day 40  Frontend → API          — React fetch() to Express backend
Day 41  Bearer token auth       — Authorization header, validation
Day 42  Environment tokens      — .env, process.env, secrets
Day 43  Error handling          — try/catch, HTTP error responses
Day 44  Swagger docs            — OpenAPI spec, documentation
Day 45  AI-powered API          — POST /ai with LLM integration
```

### Phase 4 — MLOps & Cloud (Days 46–60)

```
Day 46  MLflow                  — log_param, log_metric, experiments
Day 46a Dockerize AI API        — containerize FastAPI application
Day 47  Weights & Biases        — W&B experiment tracking
Day 48  Airflow DAG             — task dependencies, scheduling
Day 49  Kubeflow Pipeline       — ML pipeline orchestration stub
Day 50  Kubernetes Pod          — Pod YAML, deployment concepts
Day 51  TorchServe              — PyTorch model serving
Day 52  GitHub Actions CI       — automated testing on push
Day 53  AWS S3                  — boto3, bucket upload/download
Day 54  AWS EC2                 — SSH, cloud compute basics
Day 55  SageMaker               — managed ML training/deployment
Day 56  Vertex AI               — Google Cloud ML platform
Day 57  Monitoring metrics      — Prometheus-style metric logging
Day 58  Batch inference         — process large datasets offline
Day 59  Scaling simulation      — load patterns, concurrency
Day 60  End-to-end pipeline     — complete ML workflow integration
```

### Phase 5 — Data Systems & Polish (Days 61–73)

```
Day 61  Matplotlib              — line plots, data visualization
Day 62  Seaborn                 — statistical visualization, heatmaps
Day 63  Plotly                  — interactive charts
Day 64  Tableau/PowerBI         — dashboard concepts
Day 65  Apache Spark            — wordcount, distributed processing
Day 66  Kafka                   — publish-subscribe messaging
Day 67  Ray                     — parallel task execution
Day 68  JAX                     — matrix ops, GPU acceleration
Day 69  Research Repro          — deterministic seeds, pytest, artifacts
Day 70  Documentation           — technical writing, README standards
Day 71  LaTeX report            — research paper formatting
Day 72  Portfolio index         — auto-generator, HTML index
Day 73  Final polish            — cleanup, documentation complete
```

---

## Tech Stack

### AI & LLM
| Tool | Used For |
|------|---------|
| OpenAI API (GPT-4o-mini) | LLM completions |
| OpenAI Embeddings | Semantic vectors |
| HuggingFace Transformers | Pre-trained NLP models |
| SentenceTransformers | Sentence embeddings |
| LangChain | LLM application framework |
| LlamaIndex | Document Q&A |
| LangGraph | Agentic workflows |
| SpaCy | Production NLP |
| NLTK | NLP fundamentals |

### Vector Search
| Tool | Used For |
|------|---------|
| FAISS | Facebook AI Similarity Search |
| ChromaDB | Persistent embedding database |
| Pinecone | Cloud vector database |

### ML Frameworks
| Tool | Used For |
|------|---------|
| PyTorch | Neural network training |
| TensorFlow/Keras | Dense layers, Sequential models |
| scikit-learn | Classical ML algorithms |
| XGBoost | Gradient boosted trees |
| NumPy | Numerical computing |
| Pandas | Data manipulation |

### Backend & APIs
| Tool | Used For |
|------|---------|
| FastAPI | Async REST APIs |
| Flask | Lightweight web server |
| Express (Node.js) | JavaScript backend |
| Redis | In-memory caching |
| MongoDB | Document database |
| PostgreSQL | Relational database |
| SQLite | Embedded database |
| gRPC | High-performance RPC |

### MLOps & Cloud
| Tool | Used For |
|------|---------|
| MLflow | Experiment tracking |
| Weights & Biases | Model monitoring |
| Airflow | Pipeline orchestration |
| Docker | Containerization |
| Kubernetes | Container orchestration |
| GitHub Actions | CI/CD |
| AWS S3 | Object storage |
| AWS EC2 | Cloud compute |
| AWS SageMaker | Managed ML |

### Data Engineering
| Tool | Used For |
|------|---------|
| Apache Spark | Distributed data processing |
| Kafka | Event streaming |
| Ray | Parallel computing |
| JAX | Accelerated ML research |

---

## Key Projects

### Vector Search Comparison (Days 19-22)
Built the same semantic search system using three different approaches:

```
SentenceTransformers embeddings
         │
    ┌────┴──────────────────────┐
    │           │               │
    ▼           ▼               ▼
  FAISS      ChromaDB        Pinecone
(Day 20)    (Day 21)        (Day 22)
In-memory   Persistent      Cloud-native
Exact ANN   + metadata      Managed
IndexFlatL2 filtering       scalable
```

### Full-Stack AI API (Days 31-45)
Progressive build of production AI API:
```
Flask (Day 31) → FastAPI (Day 32) → Auth (Day 41) → Swagger (Day 44) → AI Endpoint (Day 45)
```

### MLflow Experiment Tracking (Day 46)
```python
with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    for epoch in range(5):
        mlflow.log_metric("loss", loss, step=epoch)
        mlflow.log_metric("accuracy", acc, step=epoch)
```

### Reproducible ML Experiment (Day 69)
```python
# Deterministic seeds for reproducibility
np.random.seed(42)
torch.manual_seed(42)
# Save metrics as artifacts
# Run pytest to validate
```

---

## Project Structure

```
building-ai-engineer-73-days/
├── phase1_core_ml/
│   ├── 01_python_basics/
│   │   ├── main.py
│   │   ├── output.txt
│   │   └── run.md
│   ├── 07_tiny_linear_regression/
│   ├── 08_small_xgboost_try/
│   └── ... (15 modules)
├── phase2_llm_nlp/
│   ├── 16_transformers_tokenize/
│   ├── 20_faiss_similarity_search/
│   ├── 23_langchain_basic_chain/
│   └── ... (15 modules)
├── phase3_software_ai/
│   ├── 31_flask_basic_app/
│   ├── 35_redis_cache_test/
│   ├── 45_ai_powered_api/
│   └── ... (15 modules)
├── phase4_mlops_cloud/
│   ├── 46_mlflow_log_metric/
│   ├── 50_kubernetes_pod_yaml/
│   ├── 52_github_actions_ci/
│   └── ... (15 modules)
├── phase5_data_systems_polish/
│   ├── 65_spark_wordcount/
│   ├── 69_research_repro/
│   ├── 72_portfolio_index/
│   └── ... (13 modules)
├── make_index.py
└── requirements.txt
```

---

## Engineering Practices

Every module follows production-grade practices:

- **Version control**: Git with clean commit history
- **Artifact logging**: Every run produces `output.txt` proving execution
- **Error handling**: Graceful failure with informative error messages
- **Documentation**: `run.md` with setup and execution instructions
- **Testing**: `pytest` for reproducibility-critical modules
- **Environment management**: `.env` files for secrets, never committed

---

## Challenges Overcome

**Git Large File Problem**
Accidentally committed `.venv` directory (500MB+). GitHub rejected push.
Solution: `git-filter-repo` to rewrite history, `git gc --aggressive` to clean up.

**Repository Root Error**
Initialized git at `C:\Users\akula` — entire home directory tracked.
Solution: Moved to correct directory, re-initialized with proper `.gitignore`.

**Daily Consistency**
By week two, all obvious ideas exhausted. Projects required significant research.
Solution: Pre-planned weekly themes, accepted "working > perfect", shipped every day.

---

## Author

**Yeshwanth Akula**
M.S. Computer Science — Saint Louis University (May 2026)
Focus: AI Engineering, LLM Systems, Production ML

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/yeshwanth-akula-0339a925b)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/Yesh-is-here2)

---

> *"Consistency beats perfection. 73 shipped projects teach you more than 1 planned perfect one."*
