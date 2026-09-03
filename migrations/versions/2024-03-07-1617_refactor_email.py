"""Refactor email

Revision ID: 818bb0f07e9b
Revises: 7a7d61641dd2
Create Date: 2024-03-07 16:17:12.669422

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "818bb0f07e9b"
down_revision: str | None = "7a7d61641dd2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
