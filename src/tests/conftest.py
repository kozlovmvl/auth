from uuid import UUID
from typing import Iterable

import pytest

from models.entities import User
from models.methods import UserMethods


class MockRepo:
    data = {}

    async def get(self, id: UUID, **kwargs) -> User:
        return self.data[id]

    async def list(self, **kwargs) -> Iterable[User]:
        ...

    async def save(self, obj: User):
        self.data[obj.id] = obj

    async def delete(self, obj: User):
        self.data.pop(obj.id)


@pytest.fixture()
def mock_repo():
    yield MockRepo()


@pytest.fixture()
def mock_user_methods(mock_repo):
    yield UserMethods(repo=mock_repo)
