"""Add project_views_counter column in projects model.

Revision ID: 59ff48dfd062
Revises: 9b400a3502fb
Create Date: 2024-03-23 12:20:09.822002

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "59ff48dfd062"
down_revision = "9b400a3502fb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "projects", sa.Column("project_views_counter", sa.Integer(), nullable=True)
    )
    op.alter_column(
        "topic",
        "categorys",
        existing_type=postgresql.ENUM(
            "paintings", "web_design", "photography", name="categorys"
        ),
        type_=sa.Enum("paintings", "web_design", "photography", name="categorys"),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "topic",
        "categorys",
        existing_type=sa.Enum(
            "paintings", "web_design", "photography", name="category"
        ),
        type_=postgresql.ENUM(
            "paintings", "web_design", "photography", name="categorys"
        ),
        existing_nullable=False,
    )
    op.drop_column("projects", "project_views_counter")
    # ### end Alembic commands ###
