"""Add user address to payment methods

Revision ID: d143acc929ee
Revises: e037b5354fbf
Create Date: 2022-12-04 14:35:03.964397

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d143acc929ee"
down_revision: str | None = "e037b5354fbf"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
