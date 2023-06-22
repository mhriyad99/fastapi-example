"""create posts table

Revision ID: d7ee55cf3b94
Revises: 
Create Date: 2023-06-18 12:04:05.513064

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd7ee55cf3b94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,
                              server_default=sa.text('NOW()'))
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
