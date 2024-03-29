"""initial table Person

Revision ID: 0249ed6eaeb3
Revises: 
Create Date: 2019-04-08 23:14:06.113172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0249ed6eaeb3"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "person",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nickname", sa.String(length=32), nullable=True),
        sa.Column("first_name", sa.String(length=32), nullable=True),
        sa.Column("last_name", sa.String(length=32), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("person")
    # ### end Alembic commands ###
