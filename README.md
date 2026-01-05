# 🧮 AI Math Mentor

An end-to-end multimodal AI system that solves JEE-style math problems using
RAG, multi-agent reasoning, HITL, and memory-based learning.

## Features
- Text / Image / Audio input
- OCR + ASR parsing
- Multi-agent architecture
- RAG-based solving
- Verification & explanation
- Human feedback loop
- Self-learning memory
- Streamlit UI

## Tech Stack
- Python, Streamlit
- FAISS, SentenceTransformers
- Gemini API
- SymPy
- SQLite/JSON Memory

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py


## 🏗️ System Architecture

```mermaid
flowchart LR
    User -->|Text / Image / Audio| UI[Streamlit UI]

    UI --> Parser[Parser Agent]
    Parser --> Router[Intent Router Agent]

    Router --> Solver[Solver Agent]
    Solver -->|Query| RAG[RAG Pipeline]
    RAG -->|Context| Solver

    Solver --> Verifier[Verifier / Critic Agent]
    Verifier --> Explainer[Explainer / Tutor Agent]

    Explainer --> UI

    Verifier -->|Low Confidence| HITL[Human-in-the-Loop]
    HITL --> Parser

    Solver --> Memory[Memory Store]
    Verifier --> Memory
    Explainer --> Memory
    HITL --> Memory

    Memory -->|Similar Problems| Solver
