import models as models
from sqlalchemy.orm import Session

def get_company(db: Session, id: int):
    return db.query(models.Company).filter(models.Company.id == id).first()
