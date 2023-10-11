from sqlalchemy import  Column, Integer, String, Float, Date, Boolean, ForeignKey
from database import Base

class Company(Base):
    __tablename__ = "company"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    reg_code = Column(String(7), unique=True, nullable=False, index=True)
    created_at = Column(Date, nullable=False)
    
class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True)
    is_person = Column(Boolean, nullable=False)
    share_amount = Column(Float, nullable=False)
    is_founder = Column(Boolean, nullable=False)    
    
class Membership(Base):
    __tablename__ = "membership"
    
    id = Column(Integer, primary_key=True, index=True)
    capital = Column(Integer, default=0, nullable=False)
    member_id = Column(Integer,  ForeignKey("member.id"), nullable=False)
    copmany_id=Column(Integer, ForeignKey("company.id"), nullable=False)
        
class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    personal_code = Column(String(11), unique=True, nullable=False, index=True)



