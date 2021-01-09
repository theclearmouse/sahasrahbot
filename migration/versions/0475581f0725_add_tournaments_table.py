"""add tournaments table

Revision ID: 0475581f0725
Revises: ac7f3aaeb08a
Create Date: 2021-01-09 12:34:12.600680

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0475581f0725'
down_revision = 'ac7f3aaeb08a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tournaments',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('schedule_type', sa.String(length=45), nullable=True),
    sa.Column('slug', sa.String(length=45), nullable=True),
    sa.Column('guild_id', mysql.BIGINT(display_width=20), nullable=False),
    sa.Column('helper_roles', sa.String(length=4000), nullable=True),
    sa.Column('audit_channel_id', mysql.BIGINT(display_width=20), nullable=True),
    sa.Column('commentary_channel_id', mysql.BIGINT(display_width=20), nullable=True),
    sa.Column('active', mysql.TINYINT(display_width=1), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_tournaments_type_slug', 'tournaments', ['schedule_type', 'slug'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_tournaments_type_slug', table_name='tournaments')
    op.drop_table('tournaments')
    # ### end Alembic commands ###
