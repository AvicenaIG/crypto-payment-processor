"""Store wallet_ids with invoices

Revision ID: 704cd14b069a
Revises: 389288575d54
Create Date: 2025-10-03 01:53:06.441555

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "704cd14b069a"
down_revision = "389288575d54"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement


def downgrade() -> None:
    pass  # TODO: implement
