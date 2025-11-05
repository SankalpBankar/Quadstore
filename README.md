# 🛒 QuadStore – Product Management System
A powerful **Product Management Web App** built with **FastAPI** ⚙️ (backend) and **Streamlit** 💻 (frontend).  

## 📁 Project Directory Structure 🧠💬

```
Quadstore/
│
├── backend/
│ ├── init.py        # 🗄️ Project root
│ ├── main.py        # ⚙️ Algorithm code
│ ├── models.py      # 📦 Database handling
│ ├── database.py    # 🗄️ Database 
│ 
└── frontend/
└── frontend.py       # 🖥️🎨 Streamlit app (main simulator)
│── requirements.txt  # ✅ Dependencies list
│── .gitignore        # 🛡️To exclude myenv and other temp files

```

## 💡 Tech Stack 🛠️
- **Python** 🐍 — Core programming language for logic and data handling
- **Streamlit** 🌐 — For building the interactive web interface
- **FastAPI** ⚙️ — Backend handling
- **SQLite** 🗄️ — Database
- **Swagger UI** 🧪— API Docs

## ⚙️ Setup & Installation for Quadstore 🛒📦
Follow these steps to set up the Quadstore:
### 1️⃣ Clone the Repository 📥
```sh
git clone https://github.com/<your-username>/QuadStore.git
cd QuadStore
```

### 2️⃣ Create and activate virtual environment 🐍
```sh
python -m venv myenv
myenv\Scripts\activate
```

### 3️⃣ Install Dependencies �
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Backend Server ⚙️
```sh
cd backend
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
✅ Server will start at → http://127.0.0.1:8000
📘 Interactive Docs → http://127.0.0.1:8000/docs

### 5️⃣ Run the Frontend App 💻
```sh
cd frontend
pip install streamlit requests
streamlit run frontend.py
```
🌐 App will open automatically → http://localhost:8501

## 🛠️ Troubleshooting 🚨

### 1. ConnectionError ❌:
Backend not running
```sh
uvicorn backend.main:app --reload
```

### 2. PowerShell Activation Error ⚡
Open PowerShell as Administrator and run:
```sh
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3. AttributeError 
Virtual env not activated
```sh
myenv\Scripts\activate
```

## 💻⚙️Contributions
### 1️⃣ Sankalp Bankar (A7-B1-17)
### 2️⃣ Anish Makhija  (A7-B1-01)
### 3️⃣ Deeya Saoji    (A7-B1-10)
### 4️⃣ Mansvi Khupse  (A7-B1-04)
