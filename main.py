from typing import Union
from fastapi import FastAPI, Depends
from typing import List, Annotated 
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import models as models
from services.company import get_company

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/company/{company_id}")
def read_item(company_id: int):
    return get_company( SessionLocal(), company_id)
    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
db_dependency =  Annotated[Session, Depends(get_db)]        