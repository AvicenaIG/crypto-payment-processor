"""removed balance field

Revision ID: 1c465e341efa
Revises: a27789cb7b2a
Create Date: 2020-10-09 23:29:44.645464

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1c465e341efa"
down_revision: str | None = "a27789cb7b2a"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
