from typing import Protocol
from uuid import UUID

from api.users.dto import UserModel
from models.methods import UserMethodsProtocol


class UserUsecaseProtocol(Protocol):
    async def get(self, user_id: UUID) -> UserModel:
        ...

    async def create(self, data: UserModel) -> UUID:
        ...

    async def update(self, data: UserModel) -> None:
        ...

    async def delete(self, user_id: UUID) -> None:
        ...


class UserUsecase:
    def __init__(self, user_methods: UserMethodsProtocol):
        self.user_methods = user_methods

    async def get(self, user_id: UUID) -> UserModel:
        return await self.user_methods.get(id=user_id)

    async def create(self, data: UserModel) -> UUID:
        await self.user_methods.save(data)
        return data.id

    async def update(self, data: UserModel) -> None:
        await self.user_methods.save(data)

    async def delete(self, user_id: UUID) -> None:
        user = await self.user_methods.get(id=user_id)
        await self.user_methods.delete(user)
