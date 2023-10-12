from fastapi import FastAPI, Depends
from typing import  Annotated 
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
import models as models
from services.company import get_company_data, create_company, get_all_companies

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/company/{company_id}")
def get_company(company_id: int):
    return get_company_data(SessionLocal(), company_id)

@app.get("/companies")
def get_companies():
    return get_all_companies(SessionLocal())
    
@app.post("/company")
def post_company(name: str, reg_code: str, created_at: str):
    return create_company(SessionLocal(), name, reg_code, created_at)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
db_dependency =  Annotated[Session, Depends(get_db)]        