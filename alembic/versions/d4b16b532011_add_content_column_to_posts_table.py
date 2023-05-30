"""add content column to posts table

Revision ID: d4b16b532011
Revises: 0a4bba31ccbb
Create Date: 2023-05-30 12:41:55.950092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b16b532011'
down_revision = '0a4bba31ccbb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
