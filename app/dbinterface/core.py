import os

from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
DB_DIALECT = os.getenv("DB_DIALECT")


engine = create_engine(
    URL.create(
        DB_DIALECT,
        username=DB_USER,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

AMOUNT_LIMIT = 1000
