import models as models
from sqlalchemy.orm import Session


def get_all_people(db: Session):
    people = db.query(models.Person).all()

    return people

def create_person(db: Session, name: str, personal_code: str):
    new_person = models.Person(name = name, personal_code = personal_code)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    
    return new_person