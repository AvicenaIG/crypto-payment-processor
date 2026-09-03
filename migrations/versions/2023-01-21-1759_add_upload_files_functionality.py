"""Add upload files functionality

Revision ID: 5e08deebdb74
Revises: 12f53bb6513c
Create Date: 2023-01-21 17:59:29.322651

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5e08deebdb74"
down_revision: str | None = "12f53bb6513c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
