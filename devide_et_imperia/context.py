from flask import g

from devide_et_imperia.service.repo import UserRepo, AbstractUserRepo, AbstractGroupRepo, GroupRepo


def get_user_repo() -> AbstractUserRepo:
    if 'user_repo' not in g:
        g.user_repo = UserRepo()
    return g.user_repo


def get_group_repo() -> AbstractGroupRepo:
    if 'group_repo' not in g:
        g.group_repo = GroupRepo()
    return g.group_repo
