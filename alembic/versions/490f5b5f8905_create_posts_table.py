"""Create posts table

Revision ID: 490f5b5f8905
Revises: 
Create Date: 2022-12-12 19:01:30.362635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "490f5b5f8905"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
