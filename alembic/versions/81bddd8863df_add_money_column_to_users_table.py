"""Add money column to users table

Revision ID: 81bddd8863df
Revises: 5718752d9ad1
Create Date: 2024-11-27 18:15:44.757847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81bddd8863df'
down_revision: Union[str, None] = '5718752d9ad1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('money', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'money')
    # ### end Alembic commands ###
