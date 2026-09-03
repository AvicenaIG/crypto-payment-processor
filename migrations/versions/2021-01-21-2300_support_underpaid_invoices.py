"""Support underpaid invoices

Revision ID: efe99ea3b809
Revises: 7208e2a9a8e8
Create Date: 2021-01-21 23:00:01.119398

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "efe99ea3b809"
down_revision: str | None = "7208e2a9a8e8"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
