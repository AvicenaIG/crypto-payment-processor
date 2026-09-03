"""Add ETH

Revision ID: 69b52fb159ed
Revises: d42daa00adf8
Create Date: 2022-03-17 12:36:38.746587

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "69b52fb159ed"
down_revision: str | None = "d42daa00adf8"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
