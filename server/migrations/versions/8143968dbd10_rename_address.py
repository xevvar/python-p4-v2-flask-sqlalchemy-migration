"""rename address

Revision ID: 8143968dbd10
Revises: 7f267889c7be
Create Date: 2024-09-03 18:06:42.342535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8143968dbd10'
down_revision = '7f267889c7be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
