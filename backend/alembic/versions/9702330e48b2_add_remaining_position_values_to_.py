"""add remaining position values to eligibleposition enum

Revision ID: 9702330e48b2
Revises: 3da4df4de77a
Create Date: 2026-07-05 06:22:42.656195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9702330e48b2'
down_revision: Union[str, Sequence[str], None] = '3da4df4de77a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    values_to_add = [
        "P", "C", "1B", "2B", "3B", "SS", "OF", # MLB
        "PG", "SG", "SF", "PF", "G", "F", "UTIL", # NBA
        "W", "D", "GOLFER", "Super FLEX" # NHL, PGA, CFB
    ]
    for value in values_to_add:
        op.execute(f"ALTER TYPE eligibleposition ADD VALUE IF NOT EXISTS '{value}'")


def downgrade() -> None:
    """Downgrade schema."""
    pass
