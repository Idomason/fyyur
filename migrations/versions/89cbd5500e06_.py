"""empty message

Revision ID: 89cbd5500e06
Revises: 64aa06c1fd54
Create Date: 2022-07-25 09:58:51.549614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89cbd5500e06'
down_revision = '64aa06c1fd54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    # ### end Alembic commands ###
