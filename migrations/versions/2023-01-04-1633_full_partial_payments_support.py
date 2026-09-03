"""Full partial payments support

Revision ID: 2d6563c7943d
Revises: 3801b9cf3278
Create Date: 2023-01-04 16:33:12.956781

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2d6563c7943d"
down_revision: str | None = "3801b9cf3278"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
