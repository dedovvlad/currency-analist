"""empty message

Revision ID: 5afc2bbe0094
Revises: 
Create Date: 2022-07-12 12:12:06.842017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5afc2bbe0094'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('telegram_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.String(), nullable=True),
    sa.Column('update_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_telegram_groups_chat_id'), 'telegram_groups', ['chat_id'], unique=True)
    op.create_index(op.f('ix_telegram_groups_id'), 'telegram_groups', ['id'], unique=False)
    op.create_index(op.f('ix_telegram_groups_update_id'), 'telegram_groups', ['update_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_telegram_groups_update_id'), table_name='telegram_groups')
    op.drop_index(op.f('ix_telegram_groups_id'), table_name='telegram_groups')
    op.drop_index(op.f('ix_telegram_groups_chat_id'), table_name='telegram_groups')
    op.drop_table('telegram_groups')
    # ### end Alembic commands ###
