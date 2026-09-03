"""Add recommended fee

Revision ID: 927a773be59d
Revises: d8515a8b706e
Create Date: 2021-01-22 19:48:25.437634

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "927a773be59d"
down_revision: str | None = "d8515a8b706e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
