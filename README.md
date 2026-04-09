📦 ItemVault_app

A production-ready FastAPI backend featuring secure JWT authentication, PostgreSQL integration, structured Alembic migrations, and a clean service-layer architecture. ItemVault_app provides robust item management with full CRUD operations, advanced filtering, sorting, and pagination — designed to reflect real-world backend engineering practices.

🚀 Features

JWT Authentication
Secure login & registration with hashed passwords.

PostgreSQL Database
Reliable relational storage for users and items.

Alembic Migrations
Alembic is used to manage database schema changes in a controlled way. Instead of manually modifying tables, we create migration files that describe the change(Like adding/deleting a column later) These migrations can then be applied consistently across development, testing, and production environments.

Modular Architecture
Clean separation of concerns using Routers → Services → Models.

CRUD Operations for Items
Create, read, update, and delete item records.

Advanced Query Features
Filtering, sorting, and pagination support for flexible data retrieval.

Environment Variable Configuration
Sensitive settings managed through .env file.

Basic Logging
Structured logs for debugging and production observability.

🛠️ Tech Stack

Python 3.10+

FastAPI

SQLAlchemy

PostgreSQL

Alembic

Passlib (for hashing)

Python-Jose (for JWT)

🔐 Authentication Flow

Register a new user with /auth/register.

Login using /auth/login to receive a JWT access token.

Use Authorization: Bearer <token> to access protected item routes.

🧪 API Capabilities

Items Module

POST /items → Create item

GET /items → List all items

GET /items/{id} → Get item by ID

PUT /items/{id} → Update item

DELETE /items/{id} → Delete item

GET /items_filter → Filter items

GET /items_sort → Sort items

GET /items_advanced → Filter + Sort + Pagination
Auth Module

POST /auth/register

POST /auth/login

⚙️ Environment Variables (.env)

Your root .env file should include:

DATABASE_URL=postgresql://postgres:<password>@localhost/<dbname>

SECRET_KEY=<your_secret_key>

ACCESS_TOKEN_EXPIRE_MINUTES=60


Never commit .env to GitHub.

▶️ Running the App

Start the FastAPI server:
uvicorn app.main:app --reload

http://127.0.0.1:8000

📘 Database Migrations

To generate a new migration:

alembic revision --autogenerate -m "description"


To apply migrations:

alembic upgrade head

