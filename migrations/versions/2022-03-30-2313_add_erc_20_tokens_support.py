"""Add ERC-20 tokens support

Revision ID: 58f6fcd5af80
Revises: 69b52fb159ed
Create Date: 2022-03-30 23:13:36.169360

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "58f6fcd5af80"
down_revision: str | None = "69b52fb159ed"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None



def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
