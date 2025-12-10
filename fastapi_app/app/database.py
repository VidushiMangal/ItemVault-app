#CREATING DATABASE CONNECTION
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError

# 1. Load values from .env into environment
load_dotenv()

# 2. Read DATABASE_URL from env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in .env")

# 3. Set up SQLAlchemy engine & session
engine = create_engine(DATABASE_URL,pool_pre_ping=True)
try:
    with engine.connect() as conn:
        print(" Database (Postgres) Connected Successfully!")
except OperationalError as e:
    print("Database (Postgres) Connection Failed!")
    print(e)
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class for models
Base = declarative_base()





