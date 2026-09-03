"""add paid_currency to invoice

Revision ID: a27789cb7b2a
Revises: d47757e34b68
Create Date: 2020-09-12 00:07:55.231565

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a27789cb7b2a"
down_revision: str | None = "d47757e34b68"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
