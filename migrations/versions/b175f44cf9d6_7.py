"""7

Revision ID: b175f44cf9d6
Revises: affea1f8f6cb
Create Date: 2020-04-28 13:11:50.851488

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b175f44cf9d6'
down_revision = 'affea1f8f6cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ih_paper_profile', sa.Column('state', sa.String(length=1), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ih_paper_profile', 'state')
    # ### end Alembic commands ###
