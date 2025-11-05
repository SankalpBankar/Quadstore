# 🛒 QuadStore – Product Management System
A powerful **Product Management Web App** built with **FastAPI** ⚙️ (backend) and **Streamlit** 💻 (frontend).  

## 📁 Project Directory Structure 🧠💬

```
Quadstore/
│
├── backend/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── database.py
│
└── frontend/
└── frontend.py

```

## 💡 Tech Stack 🛠️
- **Python** 🐍 — Core programming language for logic and data handling
- **Streamlit** 🌐 — For building the interactive web interface
- **FastAPI** ⚙️ — Backend handling
- **SQLite** 🗄️ — Database
- **Swagger UI ** 🧪— API Docs

## Overview
A simple full-stack Python lab project using:
- FastAPI (Backend)
- Streamlit (Frontend)
- SQLite (Database)

## How to Run

### 1. Create Environment
```
python -m venv myenv
myenv\Scripts\activate   # Windows
source myenv/bin/activate  # Linux/Mac
```

### 2. Setup Backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Access API docs: http://127.0.0.1:8000/docs

### 3. Run Frontend
```
cd frontend
pip install streamlit requests
streamlit run frontend.py
```

### 4. Use App 🎉
Add, view, update, delete products.
