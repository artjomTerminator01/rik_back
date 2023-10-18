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

def create_company(db: Session, company_data: dict):
    check_existing_company(db, company_data.name, company_data.reg_code)
    new_company = models.Company(name=company_data.name, reg_code=company_data.reg_code, created_at=company_data.created_at, capital = company_data.capital)
    db.add(new_company)
    
    for member in company_data.members:
        if member['is_person']:
            new_membership = models.Membership(
                capital=member['capital'],
                is_person=True,
                role=member['role'],
                company_reg_code=company_data.reg_code,
                member_person_id=member['id']
            )
        else: 
            new_membership = models.Membership(
                capital=member['capital'],
                is_person=False,
                role=member['role'],
                company_reg_code=company_data.reg_code,
                member_company_id=member['id']
            )
        db.add(new_membership)

    db.commit()
    
    return new_company

def update_capital(db: Session, reg_code: str, capital: int):
    company = db.query(models.Company).filter(models.Company.reg_code == reg_code).first()
    print(capital)
    if company:
        company.capital += capital
        db.commit()
        return company
    return None

def update_membership_capital(db: Session, membership_data: dict ):
    membership = db.query(models.Membership).filter(models.Membership.id == membership_data.membership_id).first()
    
    if membership:
        capital_dif = membership_data.capital- membership.capital 
        update_capital(db, membership.company_reg_code, capital_dif)
        membership.capital = membership_data.capital
        db.commit()
        return membership
    return None

def add_new_member(db: Session, membership_data: dict):
    new_membership = models.Membership(
        capital=membership_data.capital,
        is_person=membership_data.is_person,
        role=membership_data.role,
        company_reg_code=membership_data.company_reg_code
    )
    if membership_data.is_person:
        new_membership.member_person_id = membership_data.member_person_id
    else:
        new_membership.member_company_id = membership_data.member_company_id
    db.add(new_membership)
    db.commit()
    update_capital(db, membership_data.company_reg_code, membership_data.capital)
    return new_membership

def get_company_members(db, reg_code):
    memberships = db.query(models.Membership).filter(models.Membership.company_reg_code == reg_code).all()
    members = []

    for membership in memberships:
        is_person = membership.is_person
        if is_person:
            member = db.query(models.Person).filter(models.Person.id == membership.member_person_id).first()
        else:
            member = db.query(models.Company).filter(models.Company.id == membership.member_company_id).first()
        if member:
            member_info = {
                'is_person': is_person,
                'name': member.name,
                'capital': membership.capital,
                'role': membership.role,
                'membership_id': membership.id
            }
            if is_person:
                member_info['personal_code'] = member.personal_code
            else:
                member_info['reg_code'] = member.reg_code
            members.append(member_info)

    return members

