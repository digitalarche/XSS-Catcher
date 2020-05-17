"""cleaner model

Revision ID: 8df646aeb452
Revises: 
Create Date: 2020-04-03 15:12:04.886819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8df646aeb452'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('first_login', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.CHAR(length=6), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('XSS',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('header', sa.TEXT(), nullable=True),
    sa.Column('ip_addr', sa.String(length=15), nullable=True),
    sa.Column('data', sa.TEXT(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('xss_type', sa.String(length=9), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('XSS')
    op.drop_table('client')
    op.drop_table('user')
    # ### end Alembic commands ###