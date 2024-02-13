"""corrected the missing  Column in the Tables

Revision ID: a06ec14c04ce
Revises: f6b193ccf490
Create Date: 2024-02-13 13:49:31.582513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a06ec14c04ce'
down_revision = 'f6b193ccf490'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
