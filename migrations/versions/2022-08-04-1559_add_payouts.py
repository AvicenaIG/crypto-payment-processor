"""Add payouts

Revision ID: be1f56ed9798
Revises: a050d461a6c1
Create Date: 2022-08-04 15:59:41.375425

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "be1f56ed9798"
down_revision: str | None = "a050d461a6c1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
