"""Add email verification

Revision ID: 12f53bb6513c
Revises: 7d87040b9f50
Create Date: 2023-01-20 02:27:02.128776

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "12f53bb6513c"
down_revision: str | None = "7d87040b9f50"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
