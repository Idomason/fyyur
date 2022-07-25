"""Fixed a bug

Revision ID: abcedef07361
Revises: d0f44a1d25ac
Create Date: 2022-07-25 14:36:28.324459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abcedef07361'
down_revision = 'd0f44a1d25ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('artists', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
