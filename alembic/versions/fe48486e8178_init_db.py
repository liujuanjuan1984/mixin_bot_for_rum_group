"""init db

Revision ID: fe48486e8178
Revises: 
Create Date: 2022-09-08 12:33:26.940301

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "fe48486e8178"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_messages_id", table_name="messages")
    op.drop_table("messages")
    op.add_column("keystores", sa.Column("is_rss", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("keystores", "is_rss")
    op.create_table(
        "messages",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("message_id", sa.VARCHAR(length=36), nullable=True),
        sa.Column("replied", sa.BOOLEAN(), nullable=True),
        sa.Column("sent_to_rum", sa.BOOLEAN(), nullable=True),
        sa.Column("quote_message_id", sa.VARCHAR(length=36), nullable=True),
        sa.Column("conversation_id", sa.VARCHAR(length=36), nullable=True),
        sa.Column("user_id", sa.VARCHAR(length=36), nullable=True),
        sa.Column("text", sa.VARCHAR(), nullable=True),
        sa.Column("category", sa.VARCHAR(length=36), nullable=True),
        sa.Column("timestamp", sa.VARCHAR(), nullable=True),
        sa.Column("created_at", sa.VARCHAR(), nullable=True),
        sa.Column("updated_at", sa.VARCHAR(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("message_id"),
    )
    op.create_index("ix_messages_id", "messages", ["id"], unique=False)
    # ### end Alembic commands ###
