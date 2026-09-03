"""Fix html templates rendering

Revision ID: 5bf0a0845afb
Revises: e027e56adb58
Create Date: 2021-01-03 21:45:14.779772

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.sql import expression

# revision identifiers, used by Alembic.
revision: str = "5bf0a0845afb"
down_revision: str | None = "e027e56adb58"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
