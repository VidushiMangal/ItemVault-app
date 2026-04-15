# 📦 ItemVault_app

A production-ready FastAPI backend featuring secure JWT authentication, PostgreSQL integration, structured Alembic migrations, and a clean service-layer architecture.ItemVault_app provides robust item management with full CRUD operations, advanced filtering, sorting, and pagination — designed to reflect real-world backend engineering practices.

# 🌍 Live Deployment

🚀 **Live API:** https://your-app-name.onrender.com
📘 **Swagger Docs:** https://itemvault-app.onrender.com/docs

Deployed using: 
* Render (Backend Hosting)
* Neon (Serverless PostgreSQL)

# 🚀 Features

**JWT Authentication**: Secure login & registration with hashed passwords.

**PostgreSQL Database**: Cloud-hosted database using Neon (serverless PostgreSQL).

**Alembic Migrations**:Database schema changes are managed using Alembic migrations, ensuring consistency across development and production environments.

**Modular Architecture**:Clean separation of concerns using:Routers → Services → Models

**CRUD Operations**:Create, read, update, and delete item records.

**Advanced Query Features**:Filtering, sorting, and pagination support.

**Environment-Based Configuration**:Sensitive data managed via environment variables (production-ready approach).

**Logging**:Basic logging for debugging and monitoring.

# 🛠️ Tech Stack

* Python 3.10+
* FastAPI
* SQLAlchemy
* PostgreSQL (Neon)
* Alembic
* Passlib (password hashing)
* Python-Jose (JWT)

# 🔐 Authentication Flow

1. Register a new user → `/auth/register`
2. Login → `/auth/login` → receive JWT token
3. Use token:
   Authorization: Bearer <token>
4. Access protected routes

# 🧪 API Endpoints

## 📦 Items Module

* POST `/items` → Create item
* GET `/items` → List items
* GET `/items/{id}` → Get item
* PUT `/items/{id}` → Update item
* DELETE `/items/{id}` → Delete item

### Advanced:

* GET `/items_filter`
* GET `/items_sort`
* GET `/items_advanced`

## 🔐 Auth Module

* POST `/auth/register`
* POST `/auth/login`

# ⚙️ Environment Variables

Set the following variables in your environment (Render / local):

DATABASE_URL=your_neon_connection_string
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

⚠️ Never commit secrets to GitHub.

# ▶️ Running Locally

uvicorn app.main:app --reload
Open:
http://127.0.0.1:8000/docs

# ☁️ Deployment

This project is deployed using:
* Render for backend hosting
* Neon for PostgreSQL database

Steps:
1. Push code to GitHub
2. Connect repository to Render
3. Add environment variables
4. Deploy using Uvicorn start command

# 📘 Database Migrations

Create migration:
alembic revision --autogenerate -m "description"

Apply migration:
alembic upgrade head

# 🧠 Key Highlights

* Production-ready FastAPI backend
* Real cloud deployment (Render + Neon)
* Secure authentication system
* Clean scalable architecture
* Interview-ready project

---
