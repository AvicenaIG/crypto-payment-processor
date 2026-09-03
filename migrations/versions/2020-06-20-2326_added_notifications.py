"""Added notifications

Revision ID: bbeb9365b195
Revises: 9232980a793a
Create Date: 2020-06-20 23:26:09.349131

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "bbeb9365b195"
down_revision: str | None = "9232980a793a"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
