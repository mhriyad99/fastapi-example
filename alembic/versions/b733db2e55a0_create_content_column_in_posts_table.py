"""create content column in posts table

Revision ID: b733db2e55a0
Revises: d7ee55cf3b94
Create Date: 2023-06-18 12:25:46.456146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b733db2e55a0'
down_revision = 'd7ee55cf3b94'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
