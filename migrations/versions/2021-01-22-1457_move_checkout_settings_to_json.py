"""Move checkout settings to JSON

Revision ID: d8515a8b706e
Revises: efe99ea3b809
Create Date: 2021-01-22 14:57:51.026193

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "d8515a8b706e"
down_revision: str | None = "efe99ea3b809"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
