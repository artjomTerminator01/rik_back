from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Database URL, replace with your PostgreSQL database URL
DATABASE_URL = "postgresql://postgres@localhost:5432/rik"

# Create a SQLAlchemy database engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Create the "company" table in the database
Base.metadata.create_all(bind=engine)