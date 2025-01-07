from typing import Protocol
from models.entities import User
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
