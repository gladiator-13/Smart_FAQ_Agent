# Smart FAQ Agent — Hybrid Retrieval RAG System

A modular Retrieval-Augmented Generation (RAG) system implementing and benchmarking multiple retrieval strategies for FAQ-based question answering.

This project explores the architectural trade-offs between:
- Lexical retrieval (token overlap)
- Semantic retrieval (dense embeddings)
- Hybrid retrieval (combined scoring)
- Evaluation using IR metrics (Recall@k, MRR)

---

## Project Overview

Smart FAQ Agent answers user queries by:
1. Retrieving relevant FAQ entries using configurable retrieval modes:
   - Lexical
   - Semantic (SentenceTransformer embeddings)
   - Hybrid (weighted semantic + lexical scoring)
2. Passing top-k retrieved context to an LLM (Google Gemini)
3. Generating structured, context-constrained responses
The system is designed to demonstrate proper retrieval architecture design rather than simple API usage.

---

## Retrieval Architecture
```

User Query
   ↓
Retriever (Lexical / Semantic / Hybrid)
   ↓
Top-k Ranked FAQ Candidates
   ↓
Prompt Builder
   ↓
LLM (Gemini)
   ↓
Final Answer

Hybrid Scoring Formula:
Final Score = α × Semantic Similarity + β × Lexical Overlap

This enables fine-grained discrimination between closely related concepts (e.g., pretraining vs fine-tuning). 

```
---

## Evaluation Framework

The system includes an evaluation module that measures:
- Recall@1
- Recall@3
- Mean Reciprocal Rank (MRR)
This allows empirical comparison between retrieval strategies.

 ```

| Mode     | Recall@1 | Recall@3 | MRR  |
|----------|:--------:|:--------:|:----:|
| Lexical  |  0.200   |  0.200   | 0.200|
| Semantic |  0.600   |  0.600   | 0.600|
| Hybrid   |  0.600   |  0.600   | 0.600|

```

## Project Structure
```

smart-faq-agent/
│
├── agent/
│   ├── llm.py              # Google ADK / Gemini integration
│   ├── logger.py           # Logging configuration
│   ├── memory.py           # Memory abstraction layer
│   ├── prompt.py           # Prompt construction logic
|   ├── dataloader.py       
│   │
│   └── retriever/
│       ├── lexical.py      # Keyword-based retrieval
│       ├── __init__.py
|       ├── semantic.py
|       └── hybrid.py
│
├── app.py                  # Entry point
├── evaluation_data.py
├── evaluation_runner.py
├── evaluator.py
├── requirements.txt
├── .gitignore
└── README.md
 
```

## Core Features

- Modular retrieval abstraction
- Dense embedding search (SentenceTransformers)
- Hybrid retrieval scoring
- Evaluation using standard IR metrics
- Context-constrained LLM generation
- Clean project structuring and separation of concerns

---

## Tech Stack

- Python
- SentenceTransformers (all-MiniLM-L6-v2)
- Google Gemini (via Google AI Studio)
- scikit-learn
- python-dotenv

---

## Environment Setup

Create a `.env` file in root: 
GOOGLE_API_KEY=your_google_ai_studio_key

Install dependencies: pip install -r requirements.txt

Run the app: python app.py


---

## Key Learnings

This project demonstrates:
1. Retrieval system design
2. Hybrid scoring strategies
3. Embedding limitations and trade-offs
4. Information Retrieval metrics
5. Modular AI agent architecture
6. Proper Git version control workflow

---

## Learning Focus

This project emphasizes:
- Agent modularity
- Retrieval-Augmented Generation fundamentals
- Clean engineering practices
- Secure secret management
- Git hygiene and version control discipline

---

## Author
Built as part of a structured progression into retrieval systems and AI agent architecture.

