"""add album_genre attri

Revision ID: 56dc661e82c9
Revises: 5fc0d398fd36
Create Date: 2024-03-10 18:21:41.020429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56dc661e82c9'
down_revision = '5fc0d398fd36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('albums', schema=None) as batch_op:
        batch_op.add_column(sa.Column('album_genre', sa.String(length=60), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('albums', schema=None) as batch_op:
        batch_op.drop_column('album_genre')

    # ### end Alembic commands ###
