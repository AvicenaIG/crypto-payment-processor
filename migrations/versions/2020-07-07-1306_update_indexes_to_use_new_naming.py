"""Update indexes to use new naming conventions

Revision ID: 03e98a49599c
Revises: c0fb4e374830
Create Date: 2020-07-07 13:06:06.204241

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "03e98a49599c"
down_revision: str | None = "c0fb4e374830"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
