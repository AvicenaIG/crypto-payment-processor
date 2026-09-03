"""Add store theme settings

Revision ID: 73d794ea10e2
Revises: e627af4b2a1c
Create Date: 2021-11-20 23:54:22.931026

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "73d794ea10e2"
down_revision: str | None = "e627af4b2a1c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
