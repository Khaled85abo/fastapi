"""Add company type

Revision ID: 48dd61d47577
Revises: 6c63bfbe4ef5
Create Date: 2024-02-21 16:00:35.732052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48dd61d47577'
down_revision: Union[str, None] = '6c63bfbe4ef5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company_types',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('companey_type')
    op.drop_table('companey_types')
    op.add_column('company', sa.Column('company_type_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'company', 'company_types', ['company_type_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'company', type_='foreignkey')
    op.drop_column('company', 'company_type_id')
    op.create_table('companey_types',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='companey_types_pkey')
    )
    op.create_table('companey_type',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='companey_type_pkey')
    )
    op.drop_table('company_types')
    # ### end Alembic commands ###
