# QuadStore – Product Management System

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
