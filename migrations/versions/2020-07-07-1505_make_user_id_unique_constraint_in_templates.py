"""Make user_id a unique constraint in templates

Revision ID: 5f88cc45615c
Revises: 03e98a49599c
Create Date: 2020-07-07 15:05:35.893167

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5f88cc45615c"
down_revision: str | None = "03e98a49599c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
