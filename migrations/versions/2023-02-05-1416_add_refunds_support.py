"""Add refunds support

Revision ID: 427d55a6fd22
Revises: 5e08deebdb74
Create Date: 2023-02-05 14:16:00.051868

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "427d55a6fd22"
down_revision: str | None = "5e08deebdb74"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
