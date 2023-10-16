from fastapi import FastAPI, Depends
from typing import  Annotated 
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
import models as models
from services.company import get_company_data, create_company, get_all_companies, add_new_member,update_membership_capital
from services.person import create_person, get_all_people

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

class CompanyCreate(BaseModel):
    name: str
    regCode: str
    createdAt: str
    capital: int
    members: list
    
class MembershipCreate(BaseModel):
    is_person: bool
    capital: int
    role: str
    company_reg_code: str
    member_person_id: int | None
    member_company_id: int | None
    
class UpdateMembershipCapital(BaseModel):
    membership_id: int
    capital: int
    
class PersonCreate(BaseModel):
    name: str
    personalCode: str

@app.get("/company/{reg_code}")
def get_company(reg_code: str):
    return get_company_data(SessionLocal(), reg_code)

@app.get("/companies")
def get_companies():
    return get_all_companies(SessionLocal())
    
@app.post("/company")
def post_company(company_data: CompanyCreate):
    name = company_data.name
    reg_code = company_data.regCode
    created_at = company_data.createdAt
    capital = company_data.capital
    members = company_data.members
    
    return create_company(SessionLocal(), name, reg_code, created_at, capital, members)

@app.post("/company/membership")
def post_membership(membership_data: MembershipCreate):
    return add_new_member(SessionLocal(), membership_data)

@app.post("/company/membership/capital")
def post_membership_capital(membership_data: UpdateMembershipCapital ):
    return update_membership_capital(SessionLocal(), membership_data)

# @app.post("/person")
# def post_person(person_data: PersonCreate):
#     name = person_data.name
#     personal_code = person_data.personalCode
#     return create_person(SessionLocal(), name, personal_code)

@app.get("/people")
def get_people():
    return get_all_people(SessionLocal())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
db_dependency =  Annotated[Session, Depends(get_db)]        