# Building AI Engineer in 73 Days

A structured, phase-wise roadmap documenting my journey to becoming a production-ready AI Engineer through hands-on implementation across machine learning, LLMs, software systems, MLOps, and data engineering.

---

## Project Structure

### Phase 1 — Core ML Foundations
- Python, NumPy, Pandas
- Classical Machine Learning workflows
- PostgreSQL integration
- Docker & Docker Compose
- End-to-end mini ML pipeline

### Phase 2 — LLM & NLP Systems
- Text preprocessing and embeddings
- Transformer fundamentals
- Prompt engineering
- Retrieval-Augmented Generation (RAG)
- Local and API-based LLM integration

### Phase 3 — Software Engineering for AI
- FastAPI services for ML/LLM models
- Backend architecture & modular design
- Testing, logging, and configuration management

### Phase 4 — MLOps & Cloud
- Experiment tracking
- Model versioning
- Containerized deployment
- CI/CD for ML systems
- Cloud deployment fundamentals

### Phase 5 — Data Systems & Production Polish
- Data pipelines
- Vector databases
- Scalable inference design
- Production-ready AI system architecture

---

## Goals

- Transition from **ML learner → AI Engineer**
- Build **real, deployable AI systems**
- Maintain **clean engineering practices**
- Document the **complete learning journey publicly**

---

## Tech Stack

- Python
- NumPy, Pandas, Scikit-learn
- PostgreSQL
- Docker & Docker Compose
- FastAPI
- LLM tooling & vector databases (Phase 2+)

---

## How to Run (Phase 1 Example)

```bash
# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Postgres via Docker
cd phase1_core_ml/14_docker_compose_db
docker compose up -d

# Test DB connection
python ../06_postgres_connection_test/main.py
