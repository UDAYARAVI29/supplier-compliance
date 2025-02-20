import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables.
# Ensure the URL uses the 'postgresql+psycopg2' dialect.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:1234@localhost/supplier_compliance")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
