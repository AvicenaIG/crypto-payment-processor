"""Add plugin data

Revision ID: 3801b9cf3278
Revises: d143acc929ee
Create Date: 2022-12-18 21:40:23.649600

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3801b9cf3278"
down_revision: str | None = "d143acc929ee"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def add_json_field(table_name: str, column_name: str) -> None:
    pass  # TODO: implement


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
