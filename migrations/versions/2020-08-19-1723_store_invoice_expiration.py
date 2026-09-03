"""Store invoice expiration

Revision ID: a2891d77e92b
Revises: 65986008ad26
Create Date: 2020-08-19 17:23:37.273115

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a2891d77e92b"
down_revision: str | None = "65986008ad26"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
