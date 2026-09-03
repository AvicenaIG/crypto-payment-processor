"""Add user_id to every model

Revision ID: c0fb4e374830
Revises: 43bab6d0af5b
Create Date: 2020-07-06 19:50:51.353165

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c0fb4e374830"
down_revision: str | None = "43bab6d0af5b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade_data() -> None:
    pass  # TODO: implement


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
