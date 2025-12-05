# 📦 FastAPI Item Management API

A simple and clean backend API built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.  
This project demonstrates my self-learning journey in backend development through building a real, database-backed CRUD system.

The goal of this project was to understand:
- FastAPI fundamentals  
- REST API design  
- SQLAlchemy ORM  
- Database CRUD operations  
- Query parameters (filter, sort, pagination)  
- Clean project structure using services and models  

## 🚀 Features

- Full CRUD operations (Create, Read, Update, Delete)
- PostgreSQL database integration
- SQLAlchemy ORM models
- Pydantic request validation
- Query-based filtering
- Sorting (price, name)
- Pagination (skip/limit)
- Clean “service layer” architecture
- Basic FastAPI exception handling (HTTPException)

## 🛠 Tech Stack

- **Python 3.x**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **PostgreSQL**
- **Uvicorn**

---

## 📁 Project Structure

fastapi_app/
│
├── app/
│ ├── main.py
│ ├── database.py
│ │
│ ├── routers/
│ │ ├── items.py
│ │
│ ├── models/
│ │ ├── item_model.py # Pydantic request model
│ │ ├── item_db.py # SQLAlchemy DB model
│ │
│ ├── services/
│ │ ├── item_service.py # CRUD business logic
│ │
│ ├── schemas/
│ │ ├── item_schema.py # Response schema
│ │
│ ├── init.py
│
├── requirements.txt
├── README.md
└── .env (ignored in git)


---

## 🗄 Database Model (Item)

| Field       | Type    | Description          |
|------------|---------|----------------------|
| id         | Integer | Primary key          |
| name       | String  | Item name            |
| price      | Float   | Item price           |
| description| String  | Optional description |

---

## 🔗 API Endpoints

### ➤ Create Item  
`POST /items`
```json
{
  "name": "Laptop",
  "price": 85000,
  "description": "Gaming laptop"
}

➤ Get All Items : GET /items

➤ Get Single Item : GET /items/{item_id}

➤ Update Item : PUT /items/{item_id}

➤ Delete Item: DELETE /items/{item_id}

➤ Filter Items : GET /items_filter?min_price=100&max_price=500

➤ Sort Items : GET /items_sort?order_by=price
Options: price/-price/name

➤ Advanced Filtering + Sorting + Pagination : GET /items_advanced?skip=0&limit=5&order_by=price&min_price=100

▶️ Running the Project Locally
1. Clone the repository
git clone <your-repo-url>
cd fastapi_app

2. Create virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

4. Setup PostgreSQL

Create a database named: fastapi_db

5. Add .env file
DATABASE_URL=postgresql://postgres:<YOUR_PASSWORD>@localhost/fastapi_db

6. Run the API -- uvicorn app.main:app --reload

7. Access API Docs

Swagger UI:

http://127.0.0.1:8000/docs


🎯 Learning Highlights

Through this project, I learned:

How to build and structure REST APIs with FastAPI

How to use SQLAlchemy ORM for DB operations

How to validate data using Pydantic models

How to implement CRUD API patterns

How to create clean architecture using routers + service layer

How to use query parameters for filtering and pagination

This project reflects my self-learning progress and forms part of my portfolio as I prepare for Python developer roles in Canada.

📌 Future Enhancements (Optional)

Add user authentication (JWT)

Add unit tests (pytest)

Deploy on Render/Railway

Add Docker support

API rate limiting

Add search functionality



