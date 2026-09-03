"""Added custom templates

Revision ID: 43bab6d0af5b
Revises: bbeb9365b195
Create Date: 2020-07-04 16:26:02.973884

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "43bab6d0af5b"
down_revision: str | None = "bbeb9365b195"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
