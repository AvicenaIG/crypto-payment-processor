"""Add unique id

Revision ID: dfc8cd8487fd
Revises: 927a773be59d
Create Date: 2021-05-13 17:41:52.402473

"""

from collections.abc import Sequence
from typing import Any

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "dfc8cd8487fd"
down_revision: str | None = "927a773be59d"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def create_constraints() -> None:
    pass  # TODO: implement


def drop_constraints() -> None:
    pass  # TODO: implement


def upgrade() -> None:
    pass  # TODO: implement


def int_alter_column(table: str, column: str, **kwargs: Any) -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
