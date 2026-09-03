"""IPN support

Revision ID: 2612994d620f
Revises: 23db42f6e0e7
Create Date: 2020-01-19 18:13:15.623302

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2612994d620f"
down_revision: str | None = "23db42f6e0e7"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
