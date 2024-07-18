"""create account table

Revision ID: 33e31b4b3f4d
Revises: 
Create Date: 2024-05-14 10:37:27.643389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '33e31b4b3f4d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('player', 'password')


def downgrade() -> None:
    pass
