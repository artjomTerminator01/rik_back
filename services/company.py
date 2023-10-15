import models as models
from sqlalchemy.orm import Session

from services.exceptions import check_existing_company

def get_all_companies(db: Session):
    companies = db.query(models.Company).all()

    for company in companies:
        company.members = get_company_members(db, company.reg_code)
    db.close()
    return companies

def get_company_data(db: Session, reg_code: str):
    company = db.query(models.Company).filter(models.Company.reg_code == reg_code).first()
    if company:
        company.members = get_company_members(db, company.reg_code)
    db.close()

    return company

def create_company(db: Session, name: str, reg_code: str, created_at: str, capital: int, members: list):
    
    check_existing_company(db, name, reg_code)
    new_company = models.Company(name=name, reg_code=reg_code, created_at=created_at, capital = capital)
    db.add(new_company)
    
    for member in members:
        if member['is_person']:
            new_membership = models.Membership(
                capital=member['capital'],
                is_person=True,
                role=member['role'],
                company_reg_code=reg_code,
                member_person_id=member['id']
            )
        else: 
            new_membership = models.Membership(
                capital=member['capital'],
                is_person=False,
                role=member['role'],
                company_reg_code=reg_code,
                member_company_id=member['id']
            )
        db.add(new_membership)

    db.commit()
    
    
    return new_company

def get_company_members(db, reg_code):
    memberships = db.query(models.Membership).filter(models.Membership.company_reg_code == reg_code).all()
    members = []

    for membership in memberships:
        if membership.is_person:
            person = db.query(models.Person).filter(models.Person.id == membership.member_person_id).first()
            if person:
                members.append({
                    'is_person': True,
                    'name': person.name,
                    'personal_code': person.personal_code,
                    'capital': membership.capital,
                    'role': membership.role
                })
        else:
            member_company = db.query(models.Company).filter(models.Company.id == membership.member_company_id).first()
            if member_company:
                members.append({
                    'is_person': False,
                    'name': member_company.name,
                    'reg_code': member_company.reg_code,
                    'capital': membership.capital,
                    'role': membership.role
                })

    return members
