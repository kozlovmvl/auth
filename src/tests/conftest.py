from typing import Iterable

import pytest

from models.entities import Token, User
from models.methods import TokenMethods, UserMethods
from models.exceptions import ObjNotFound


class MockUserRepo:
    data = []

    async def get(self, **kwargs) -> User:
        print(kwargs, self.data)
        for user in self.data:
            if all([getattr(user, key) == val for key, val in kwargs.items()]):
                return user
        raise ObjNotFound

    async def list(self, **kwargs) -> Iterable[User]:
        ...

    async def save(self, obj: User):
        for i, user in enumerate(self.data):
            if user.id == obj.id:
                self.data[i] = obj
                return
        self.data.append(obj)

    async def delete(self, obj: User):
        for i, user in enumerate(self.data):
            if user.id == obj.id:
                self.data.pop(i)


class MockTokenRepo:
    data = []

    async def get(self, **kwargs) -> Token:
        for token in self.data:
            if all([getattr(token, key) == val for key, val in kwargs.items()]):
                return token
        raise ObjNotFound

    async def save(self, obj: Token):
        self.data.append(obj)

    async def delete(self, obj: Token):
        for i, token in enumerate(self.data):
            if token.jwt == obj.jwt:
                self.data.pop(i)


@pytest.fixture()
def mock_user_repo():
    yield MockUserRepo()


@pytest.fixture()
def mock_user_methods(mock_user_repo):
    yield UserMethods(repo=mock_user_repo)


@pytest.fixture()
def mock_token_repo():
    yield MockTokenRepo()


@pytest.fixture()
def mock_token_methods(mock_token_repo):
    yield TokenMethods(repo=mock_token_repo)
