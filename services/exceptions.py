from sqlalchemy.orm import Session
from fastapi import HTTPException
import models as models

def check_existing_company(db: Session, name: str, reg_code: str):  
    existing_company = db.query(models.Company).filter(
        (models.Company.name == name) | (models.Company.reg_code == reg_code)
    ).first()
    
    if existing_company:
        raise HTTPException(status_code=404, detail="Company name or registration code already exists")

