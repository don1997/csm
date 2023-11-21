"""Added tags and association table

Revision ID: 202947db261b
Revises: 836e007c542f
Create Date: 2023-11-20 09:27:20.053584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202947db261b'
down_revision = '836e007c542f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('snippet_tags',
    sa.Column('snippet_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['snippet_id'], ['snippet.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('snippet_id', 'tag_id'),
    info={'bind_key': None}
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snippet_tags')
    op.drop_table('tag')
    # ### end Alembic commands ###