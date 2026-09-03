"""Make quantity int

Revision ID: 2b40539e8399
Revises: 2d6563c7943d
Create Date: 2023-01-04 22:17:11.864834

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2b40539e8399"
down_revision: str | None = "2d6563c7943d"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
