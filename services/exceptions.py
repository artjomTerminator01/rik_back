from sqlalchemy.orm import Session
from fastapi import HTTPException
import models as models

def check_existing_company(db: Session, name: str, reg_code: str):  
    existing_company = db.query(models.Company).filter(
        (models.Company.name == name) | (models.Company.reg_code == reg_code)
    ).first()
    
    if existing_company:
        raise HTTPException(status_code=404, detail="Company name or registration code already exists")

def check_existing_member(db: Session, member: dict, reg_code: str):
    existing_member = db.query(models.Membership).filter(
        (models.Membership.company_reg_code == reg_code) &
        (
            (member['is_person'] & (models.Membership.member_person_id == member['member_person_id'])) |
            (~member['is_person'] & (models.Membership.member_company_id == member['member_company_id']))
        )
    ).first()
    
    if existing_member:
            raise HTTPException(status_code=404, detail="This Person/Company already exists in this company membership")

    
