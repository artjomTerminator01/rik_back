import models as models
from sqlalchemy.orm import Session

def get_all_companies(db: Session):
    companies = db.query(models.Company).all()

    for company in companies:
        company.members = get_company_members(db, company.id)
    db.close()
    return companies

def get_company_data(db: Session, id: int):
    company = db.query(models.Company).filter(models.Company.id == id).first()
    if company:
        company.members = get_company_members(db, id)
    db.close()

    return company

def create_company(db: Session, name: str, reg_code: str, created_at: str):
    
    new_company = models.Company(name=name, reg_code=reg_code, created_at=created_at)
    print(new_company)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

def get_company_members(db, company_id):
    memberships = db.query(models.Membership).filter(models.Membership.company_id == company_id).all()
    members = []

    for membership in memberships:
        if membership.is_person:
            person = db.query(models.Person).filter(models.Person.id == membership.member_person_id).first()
            if person:
                members.append({
                    'is_person': True,
                    'name': person.name,
                    'personal_code': person.personal_code
                })
        else:
            member_company = db.query(models.Company).filter(models.Company.id == membership.member_company_id).first()
            if member_company:
                members.append({
                    'is_person': False,
                    'name': member_company.name,
                    'reg_code': member_company.reg_code
                })

    return members
