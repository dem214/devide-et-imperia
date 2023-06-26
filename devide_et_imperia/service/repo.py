__all__ = ['AbstractUserRepo', 'UserRepo', 'AbstractGroupRepo', 'GroupRepo']

import abc
from typing import Final

from devide_et_imperia.domain.models import User, Group
from devide_et_imperia.domain.types import GroupId, UserId

STORAGE: Final[list[Group]] = [
    Group(
        id=GroupId(1),
        title='Senators',
        users=[
            User(UserId(1), "Priscilla", "Dare"),
            User(UserId(2), "Maymie", "Steuber"),
            User(UserId(3), "Jaylon", "Dietrich"),
            User(UserId(4), "Joy", "Purdy"),
        ]
    ),
    Group(
        id=GroupId(2),
        title='Equits',
        users=[

            User(UserId(5), "Elisabeth", "Goldner"),
            User(UserId(6), "Montana", "Shanahan"),
            User(UserId(7), "Jaleel", "Johnston"),
        ]
    ),
    Group(
        id=GroupId(3),
        title='Proletarians',
        users=[
            User(UserId(8), "Mekhi", "Labadie"),
            User(UserId(9), "Bernard", "Tromp"),
            User(UserId(10), "Lillian", "Flatley"),
        ]
    )
]


class AbstractUserRepo(abc.ABC):

    @abc.abstractmethod
    def get_all(self) -> list[User]:
        ...

    @abc.abstractmethod
    def get_by_group(self, group_id: GroupId) -> list[User]:
        ...


class AbstractGroupRepo(abc.ABC):
    @abc.abstractmethod
    def get_all(self) -> list[Group]:
        ...


class UserRepo(AbstractUserRepo):
    storage = STORAGE

    def get_all(self) -> list[User]:
        return [user for group in self.storage for user in group.users]

    def get_by_group(self, group_id: GroupId) -> list[User]:
        for group in self.storage:
            if group.id == group_id:
                return list(group.users)
        return []


class GroupRepo(AbstractGroupRepo):
    storage = STORAGE

    def get_all(self) -> list[Group]:
        return list(self.storage)
