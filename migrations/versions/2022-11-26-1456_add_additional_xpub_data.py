"""Add additional xpub data

Revision ID: c471d1bec577
Revises: be1f56ed9798
Create Date: 2022-11-26 14:56:48.405282

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c471d1bec577"
down_revision: str | None = "be1f56ed9798"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
