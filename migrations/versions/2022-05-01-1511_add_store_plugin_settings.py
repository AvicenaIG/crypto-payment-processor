"""Add store plugin settings

Revision ID: 850bd53dff02
Revises: 58f6fcd5af80
Create Date: 2022-05-01 15:11:56.127624

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "850bd53dff02"
down_revision: str | None = "58f6fcd5af80"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
