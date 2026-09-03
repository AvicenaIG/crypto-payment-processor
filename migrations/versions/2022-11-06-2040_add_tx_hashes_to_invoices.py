"""Add tx hashes to invoices

Revision ID: e037b5354fbf
Revises: be1f56ed9798
Create Date: 2022-11-06 20:40:02.929345

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "e037b5354fbf"
down_revision: str | None = "c471d1bec577"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
