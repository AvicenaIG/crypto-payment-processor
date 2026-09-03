"""Added created field to each model

Revision ID: d47757e34b68
Revises: a2891d77e92b
Create Date: 2020-08-20 16:01:46.255237

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d47757e34b68"
down_revision: str | None = "a2891d77e92b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def add_creation_date(table: str) -> None:
    pass  # TODO: implement


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
