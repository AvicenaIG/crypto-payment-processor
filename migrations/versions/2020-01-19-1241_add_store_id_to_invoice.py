"""Add store_id to invoice

Revision ID: 23db42f6e0e7
Revises: f5070830387b
Create Date: 2020-01-19 12:41:26.690465

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "23db42f6e0e7"
down_revision: str | None = "f5070830387b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
