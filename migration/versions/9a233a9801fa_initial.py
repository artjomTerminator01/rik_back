"""initial

Revision ID: 9a233a9801fa
Revises: 87a9836b8ae3
Create Date: 2023-10-11 17:43:17.211530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
from models import Person, Company

revision: str = '9a233a9801fa'
down_revision: Union[str, None] = '87a9836b8ae3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)
    person =  Person(name = 'Huila gavnov', personal_code = 11111111111)
    session.add_all([person])
    session.commit()
    
    
def downgrade() -> None:
    pass
