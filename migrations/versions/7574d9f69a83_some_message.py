"""some message

Revision ID: 7574d9f69a83
Revises: efbea168e139
Create Date: 2023-02-19 13:17:35.716846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7574d9f69a83'
down_revision = 'efbea168e139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('JKSarees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('provider', sa.String(length=140), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('JKSarees', schema=None) as batch_op:
        batch_op.drop_column('provider')

    # ### end Alembic commands ###
