__all__ = ['views_bp']

from flask import Blueprint, render_template, jsonify

from devide_et_imperia import context
from devide_et_imperia.domain.types import GroupId

views_bp = Blueprint('views', __name__)


@views_bp.route('/')
def hello():
    user_repo = context.get_user_repo()
    group_repo = context.get_group_repo()
    return render_template('index.html', groups=group_repo.get_all(), users=user_repo.get_all())


@views_bp.route('/group/<int:id_>/users')
def users_of_group(id_: int):
    repo = context.get_user_repo()
    users = repo.get_by_group(GroupId(id_))
    return jsonify(users)
