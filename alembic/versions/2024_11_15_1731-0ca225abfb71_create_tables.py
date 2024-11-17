"""create tables

Revision ID: 0ca225abfb71
Revises: 
Create Date: 2024-11-15 17:31:02.603380

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "0ca225abfb71"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "llm_report",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ai_report", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_llm_report")),
    )
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("report_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["report_id"],
            ["llm_report.id"],
            name=op.f("fk_products_report_id_llm_report"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_products")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    op.drop_table("llm_report")
    # ### end Alembic commands ###
