"""add image_url to products

Revision ID: 003
Revises: 002
Create Date: 2026-03-01

"""
from alembic import op
import sqlalchemy as sa

revision = '003'
down_revision = '002'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('products',
        sa.Column('image_url', sa.String(), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('products', 'image_url')
