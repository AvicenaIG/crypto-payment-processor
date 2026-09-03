"""Add user settings field

Revision ID: 3cfad1e70305
Revises: 3214530ea234
Create Date: 2021-06-06 21:54:16.470985

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3cfad1e70305"
down_revision: str | None = "3214530ea234"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
