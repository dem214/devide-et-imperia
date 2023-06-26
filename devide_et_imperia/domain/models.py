__all__ = ['User', 'Group']

import dataclasses

from devide_et_imperia.domain.types import UserId, GroupId


@dataclasses.dataclass
class User:
    id: UserId
    first_name: str
    last_name: str


@dataclasses.dataclass
class Group:
    id: GroupId
    title: str
    users: list[User] = dataclasses.field(default_factory=list)
