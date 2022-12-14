"""Add content column to post table

Revision ID: 62423db5f79d
Revises: 490f5b5f8905
Create Date: 2022-12-14 08:52:45.123826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "62423db5f79d"
down_revision = "490f5b5f8905"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
