"""add foreign key to posts table

Revision ID: 65e6449b7e76
Revises: 1b5a1f299e4a
Create Date: 2023-05-30 12:58:56.989595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65e6449b7e76'
down_revision = '1b5a1f299e4a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', 
                          source_table='posts', referent_table='users', 
                          local_cols=['owner_id'], remote_cols=['id'], 
                          ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
