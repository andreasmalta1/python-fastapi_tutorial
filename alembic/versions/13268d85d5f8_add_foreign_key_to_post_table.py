"""Add foreign key to post table

Revision ID: 13268d85d5f8
Revises: affd5968b7ec
Create Date: 2022-12-14 09:03:54.317776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "13268d85d5f8"
down_revision = "affd5968b7ec"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
