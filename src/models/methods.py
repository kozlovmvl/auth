from typing import Protocol
from models.entities import Token, User
from models.storage import RepoProtocol


class UserMethodsProtocol(Protocol):
    async def get(self, **kwargs) -> User:
        ...

    async def save(self, user: User):
        ...

    async def delete(self, user: User):
        ...


class UserMethods:
    def __init__(self, repo: RepoProtocol):
        self.repo = repo

    async def get(self, **kwargs) -> User:
        return await self.repo.get(**kwargs)

    async def save(self, user: User):
        await self.repo.save(user)

    async def delete(self, user: User):
        await self.repo.delete(user)


class TokenMethodsProtocol(Protocol):
    async def get(self, **kwargs) -> Token:
        ...

    async def save(self, token: Token):
        ...

    async def delete(self, token: Token):
        ...


class TokenMethods:
    def __init__(self, repo: RepoProtocol):
        self.repo = repo

    async def get(self, **kwargs) -> Token:
        return await self.repo.get(**kwargs)

    async def save(self, token: Token):
        await self.repo.save(token)

    async def delete(self, token: Token):
        await self.repo.delete(token)
