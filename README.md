# FastAPI CRUD Operations 🚀

A RESTful API built using **Python and FastAPI** to demonstrate fundamental CRUD (Create, Read, Update, Delete) operations.

This project focuses on understanding backend development concepts, API development, request handling, data validation, and HTTP methods using FastAPI.

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Data Validation:** Pydantic
- **API Documentation:** Swagger UI

## 📁 Project Structure

```text
fastapi-crud-operations/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Navitha55/fastapi-crud-operations.git
```

### 2. Navigate to the Project Directory

```bash
cd fastapi-crud-operations
```

### 3. Create a Virtual Environment

```bash
python3 -m venv myenv
```

### 4. Activate the Virtual Environment

**macOS / Linux:**

```bash
source myenv/bin/activate
```

**Windows:**

```bash
myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Running the Application

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will run at:

`http://127.0.0.1:8000`

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to explore and test API endpoints.

## 🔄 CRUD Operations

The project demonstrates the four fundamental CRUD operations:

| Operation | HTTP Method | Purpose |
|---|---|---|
| Create | POST | Add a new record |
| Read | GET | Retrieve existing records |
| Update | PUT | Modify an existing record |
| Delete | DELETE | Remove a record |

## 🎯 Learning Objectives

- Understand FastAPI application structure.
- Build RESTful APIs using HTTP methods.
- Handle incoming requests and responses.
- Implement data validation using Pydantic.
- Understand API routing and endpoint development.
- Test APIs using Swagger UI.
- Manage dependencies using virtual environments.
- Practice Git and GitHub version control.

## 👩‍💻 Author

**Navitha**

- LinkedIn: [Navitha Sri](https://www.linkedin.com/in/navitha-sri-n/)

---

⭐ If you find this project useful, feel free to explore the repository!