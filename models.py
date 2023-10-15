from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from database import Base

class Company(Base):
    __tablename__ = "company"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),unique=True,  nullable=False)
    reg_code = Column(String(7), unique=True, nullable=False, index=True)
    created_at = Column(Date, nullable=False)
    capital = Column(Integer, nullable=False)

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    personal_code = Column(String(11), unique=True, nullable=False, index=True)

class Membership(Base):
    __tablename__ = "membership"
    
    id = Column(Integer, primary_key=True, index=True)
    capital = Column(Integer, default=0, nullable=False)
    is_person = Column(Boolean, nullable=False)  # Define is_person as a boolean column
    role = Column(String, nullable=False)
    company_reg_code = Column(String(7), ForeignKey("company.reg_code"), nullable=False)

    member_person_id = Column(Integer, ForeignKey("person.id"), nullable=True)
    member_company_id = Column(Integer, ForeignKey("company.id"), nullable=True)