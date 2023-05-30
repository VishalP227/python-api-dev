"""add last few columnd to posts table

Revision ID: 63232cb98388
Revises: 65e6449b7e76
Create Date: 2023-05-30 13:28:49.161691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63232cb98388'
down_revision = '65e6449b7e76'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('publised', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('published', sa.TIMESTAMP(timezone=True),  nullable=False, server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
