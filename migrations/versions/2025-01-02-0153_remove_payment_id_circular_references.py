"""Remove payment_id circular references

Revision ID: ff416380db04
Revises: c8dc03c2cf76
Create Date: 2025-01-02 01:53:52.140515

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ff416380db04"
down_revision: str | None = "c8dc03c2cf76"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
