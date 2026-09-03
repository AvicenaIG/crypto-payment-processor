"""Fix data inconsistencies

Revision ID: c8dc03c2cf76
Revises: 1c45e078409d
Create Date: 2024-08-05 23:40:17.366979

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c8dc03c2cf76"
down_revision: str | None = "1c45e078409d"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
