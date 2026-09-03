"""New backend

Revision ID: 389288575d54
Revises: ff416380db04
Create Date: 2025-09-14 12:20:07.529106

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "389288575d54"
down_revision = "ff416380db04"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def convert_to_jsonb(table: str, column: str) -> None:
    pass  # TODO: implement


def prepare_to_cascade(table: str, column1: str, column2: str) -> None:
    pass  # TODO: implement


def upgrade() -> None:
    pass  # TODO: implement



def downgrade() -> None:
    pass  # TODO: implement

