"""Store quantity with invoice

Revision ID: f5070830387b
Revises: 25165517c582
Create Date: 2020-01-07 17:51:51.217049

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f5070830387b"
down_revision: str | None = "25165517c582"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


# not thread-safe, single-threaded use only
def downgrade() -> None:
    pass  # TODO: implement
