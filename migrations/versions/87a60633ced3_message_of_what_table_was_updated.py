"""message of what table was updated

Revision ID: 87a60633ced3
Revises: 47eb4780c05c
Create Date: 2023-11-19 22:46:20.415528

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87a60633ced3'
down_revision: Union[str, None] = '47eb4780c05c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('username', sa.String(), nullable=False))
    op.drop_column('orders', 'order_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('order_id', sa.INTEGER(), nullable=False))
    op.drop_column('orders', 'username')
    # ### end Alembic commands ###