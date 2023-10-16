"""initial

Revision ID: 9a233a9801fa
Revises: 87a9836b8ae3
Create Date: 2023-10-11 17:43:17.211530

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import orm
from models import Person, Company, Membership

revision: str = '9a233a9801fa'
down_revision: Union[str, None] = '87a9836b8ae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    session.add_all([Person(name = 'John Doe', personal_code = 11111111111),
                     Person(name = 'Mart Mets', personal_code = 50105294914),
                     Person(name = 'Kati Mati', personal_code = 40208592214),
                     Company(name = 'Maxima', reg_code = 1234567, created_at = '2021-10-11', capital = 10000),
                     Company(name = 'Lidl', reg_code = 5453331, created_at = '2022-11-12', capital = 2550),
                     Membership(capital = 7000, is_person = True, role = 'founder', member_person_id = 1, company_id = 1),
                     Membership(capital = 3000, is_person = True, role = 'founder', member_person_id = 1, company_id = 2),
                     Membership(capital = 2550, is_person = False, role = 'founder', member_company_id = 1, company_id = 2),
                     ])
    session.commit()
    
    
def downgrade() -> None:
    pass
