# BoxOps

Minimalist backoffice and AI-powered assistant for managing IKEA-style furniture catalogs, inventory, and product specifications.

## Tech Stack

- **Backend:** Django, Python, LangGraph, Pydantic, ChromaDB, SQLite
- **Frontend:** React, TailwindCSS, Vite
- **Deployment:** Docker & Docker Compose

---

## Features

- **Product Management Dashboard:** Full CRUD operations to add, modify, or remove furniture items.
- **Hybrid AI Chatbot Assistant:**
  - **Structured Data (SQL):** Automatically executes tool-calling `SELECT` queries for direct facts (prices, designer, names, brief descriptions).
  - **Unstructured Knowledge (RAG):** Performs similarity searches via ChromaDB for complex, fuzzy queries (e.g., maximum weight capacity, assembly tips).
- **Real-Time UI Feedback:** Transparent workflow states displayed in the UI (*Searching database...*, *Querying RAG...*, *Compiling results...*, *Errors*).

---

## Project Structure

```text
boxops/
├── backend/
│   ├── Dockerfile
│   └── ...
├── frontend/
│   ├── Dockerfile
│   └── ...
└── docker-compose.yml
```

---

## Getting Started (Production Mode with Docker)

Make sure you have Docker and Docker Compose installed on your machine.

1. Clone the repository
```
git clone https://github.com/ubert-guertin/boxops.git
```

2. Run the application using Docker Compose
```
docker-up --build
```

3. Access the services
```
Frontend Dashboard: http://localhost:3000
Backend API: http://localhost:8000
```
