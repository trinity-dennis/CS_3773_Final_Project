"""updated_tables

Revision ID: bbef3f7dd096
Revises: c547b5ca882e
Create Date: 2023-11-14 21:39:30.579991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbef3f7dd096'
down_revision: Union[str, None] = 'c547b5ca882e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a new table with the desired structure
    op.create_table('new_books',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('img', sa.String),
        sa.Column('genre', sa.String),
        sa.Column('title', sa.String),
        sa.Column('author', sa.String),
        sa.Column('price', sa.Float)
    )

    # Copy data from the old table to the new one
    op.execute('INSERT INTO new_books SELECT * FROM books')

    # Drop the old table
    op.drop_table('books')

    # Rename the new table to the original name
    op.rename_table('new_books', 'books')

def downgrade() -> None:
    # This is a simplified downgrade; you might need to adjust it based on your needs
    op.drop_table('books')
    op.create_table('books',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('img', sa.String),
        sa.Column('genre', sa.String),
        sa.Column('title', sa.String),
        sa.Column('author', sa.String),
        sa.Column('price', sa.Float)
    )
