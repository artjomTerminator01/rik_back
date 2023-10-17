import models as models
from sqlalchemy.orm import Session


def get_all_people(db: Session):
    people = db.query(models.Person).all()

    return people