"""empty message

Revision ID: 8b2bbde8b331
Revises: 
Create Date: 2020-08-17 08:12:59.899257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b2bbde8b331'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stu_system',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('major', sa.String(length=512), nullable=False),
    sa.Column('grade', sa.String(length=64), nullable=True),
    sa.Column('stu_id', sa.String(length=64), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stu_system')
    # ### end Alembic commands ###
