"""empty message

Revision ID: 2e0164d8fb08
Revises: 
Create Date: 2022-07-16 21:19:30.227354

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "2e0164d8fb08"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "telegram_groups",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("id_chat", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("type", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_telegram_groups_id"), "telegram_groups", ["id"], unique=False)
    op.create_index(op.f("ix_telegram_groups_id_chat"), "telegram_groups", ["id_chat"], unique=True)
    op.create_index(op.f("ix_telegram_groups_title"), "telegram_groups", ["title"], unique=False)
    op.create_index(op.f("ix_telegram_groups_type"), "telegram_groups", ["type"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_telegram_groups_type"), table_name="telegram_groups")
    op.drop_index(op.f("ix_telegram_groups_title"), table_name="telegram_groups")
    op.drop_index(op.f("ix_telegram_groups_id_chat"), table_name="telegram_groups")
    op.drop_index(op.f("ix_telegram_groups_id"), table_name="telegram_groups")
    op.drop_table("telegram_groups")
    # ### end Alembic commands ###
