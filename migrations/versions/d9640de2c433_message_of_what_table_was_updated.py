"""message of what table was updated

Revision ID: d9640de2c433
Revises: a7b6c080681d
Create Date: 2023-11-18 18:34:05.904259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9640de2c433'
down_revision: Union[str, None] = 'a7b6c080681d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accessories', sa.Column('availability', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accessories', 'availability')
    # ### end Alembic commands ###