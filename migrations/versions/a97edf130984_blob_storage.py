"""Blob storage

Revision ID: a97edf130984
Revises: 1aa72356a74b
Create Date: 2023-02-20 19:22:48.814763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a97edf130984'
down_revision = '1aa72356a74b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('JKSarees', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.TEXT(),
               type_=sa.BLOB(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('JKSarees', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.BLOB(),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
