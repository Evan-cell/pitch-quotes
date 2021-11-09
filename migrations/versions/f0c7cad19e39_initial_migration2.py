"""Initial Migration2

Revision ID: f0c7cad19e39
Revises: 
Create Date: 2021-11-08 15:12:06.505224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0c7cad19e39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitchers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('roles')
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'email')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    op.drop_table('pitchers')
    # ### end Alembic commands ###