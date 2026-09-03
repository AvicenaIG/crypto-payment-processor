"""Add shipping address

Revision ID: d42daa00adf8
Revises: 73d794ea10e2
Create Date: 2022-02-25 21:19:52.102928

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d42daa00adf8"
down_revision: str | None = "73d794ea10e2"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
