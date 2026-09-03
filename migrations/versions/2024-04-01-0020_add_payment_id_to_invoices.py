"""Add payment_id to invoices

Revision ID: 1c45e078409d
Revises: 91e2cdaa49b5
Create Date: 2024-04-01 00:20:44.780863

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1c45e078409d"
down_revision: str | None = "91e2cdaa49b5"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass  # TODO: implement







def downgrade() -> None:
    pass  # TODO: implement
