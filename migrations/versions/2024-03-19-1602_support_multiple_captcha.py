"""Support multiple captcha

Revision ID: 91e2cdaa49b5
Revises: 818bb0f07e9b
Create Date: 2024-03-19 16:02:19.347055

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "91e2cdaa49b5"
down_revision: str | None = "818bb0f07e9b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
