"""Create projects and images tables.

Revision ID: 5cd3d69b90f8
Revises: 7dd0826b45b9
Create Date: 2024-03-05 16:43:11.264712

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5cd3d69b90f8'
down_revision = '7dd0826b45b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_name', sa.String(length=255), nullable=False),
    sa.Column('project_description', sa.Text(), nullable=False),
    sa.Column('project_creation_date_time', sa.DateTime(), nullable=True),
    sa.Column('project_author', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_author'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('image_uploading_date_time', sa.DateTime(), nullable=True),
    sa.Column('image_to_project', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['image_to_project'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('topic', 'categorys',
               existing_type=postgresql.ENUM('paintings', 'web_design', 'photography', name='categorys'),
               type_=sa.Enum('paintings', 'web_design', 'photography', name='categorys'),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('topic', 'categorys',
               existing_type=sa.Enum('paintings', 'web_design', 'photography', name='category'),
               type_=postgresql.ENUM('paintings', 'web_design', 'photography', name='categorys'),
               existing_nullable=False)
    op.drop_table('images')
    op.drop_table('projects')
    # ### end Alembic commands ###