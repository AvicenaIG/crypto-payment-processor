"""Added API tokens

Revision ID: 9232980a793a
Revises: 5e3ef47c70a1
Create Date: 2020-02-21 17:34:01.613248

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9232980a793a"
down_revision: str | None = "5e3ef47c70a1"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
