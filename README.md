# Smart FAQ Agent (Google ADK + Google AI Studio)

A modular AI-powered FAQ Agent built using **Google ADK** and **Google AI Studio (Gemini models)**.

This project demonstrates the step-by-step evolution of an AI agent:
- Lexical Retrieval (baseline)
- LLM-powered response generation
- Modular agent architecture
- Memory scaffolding
- Structured prompt engineering

---

## Project Overview

Smart FAQ Agent answers user queries by:

1. Retrieving relevant FAQ entries using lexical similarity
2. Passing contextual information to a Google Gemini LLM
3. Generating intelligent, structured responses

This project focuses on building AI agents **correctly and modularly**, not just calling an API.

---

## Architecture

User Query  
   ↓  
Lexical Retriever (`agent/retriever/lexical.py`)  
   ↓  
Prompt Builder (`agent/prompt.py`)  
   ↓  
LLM Module (`agent/llm.py`)  
   ↓  
Response  
   ↓  
(Optional) Memory Layer (`agent/memory.py`)  

---

## Project Structure
smart-faq-agent/
│
├── agent/
│   ├── llm.py # Google ADK / Gemini integration
│   ├── logger.py # Logging configuration
│   ├── memory.py # Memory abstraction layer
│   ├── prompt.py # Prompt construction logic
│   │
│   └── retriever/
│       ├── lexical.py # Keyword-based retrieval
│       └── init.py
│
├── app.py # Entry point
├── requirements.txt
├── .gitignore
└── README.md


---

## Core Features

- Modular agent architecture
- Keyword-based FAQ retrieval
- Prompt templating
- Google Gemini LLM integration
- Environment-based API key handling
- Clean separation of responsibilities

---

## Tech Stack

- Python
- Google ADK
- Google AI Studio (Gemini)
- python-dotenv
- Logging module

---

## Environment Setup

Create a `.env` file in root: 
GOOGLE_API_KEY=your_google_ai_studio_key

Install dependencies: pip install -r requirements.txt

Run the app: python app.py


---

## Current Limitations

- Retrieval is lexical (exact/near keyword matching)
- No semantic embedding search yet
- No vector database integration

---

## Roadmap (Next Steps)

- Implement embedding-based semantic search
- Integrate vector database (FAISS / Chroma)
- Add conversational memory buffer
- Introduce evaluation metrics
- Deploy via FastAPI

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
Built as part of a structured journey toward advanced AI Agent development using Google ADK.

