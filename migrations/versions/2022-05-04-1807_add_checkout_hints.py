"""Add checkout hints

Revision ID: a050d461a6c1
Revises: 850bd53dff02
Create Date: 2022-05-04 18:07:13.685274

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a050d461a6c1"
down_revision: str | None = "850bd53dff02"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
