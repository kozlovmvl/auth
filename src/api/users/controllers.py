from uuid import UUID

from litestar import Controller, post, patch, get, delete
from litestar.di import Provide

from models.methods import UserMethods
from storage.repo import Repository
from api.users.dto import UserModel, UserReadDTO, UserCreateDTO, UserUpdateDTO
from api.users.usecases import UserUsecaseProtocol, UserUsecase


async def provide_user_usecase() -> UserUsecaseProtocol:
    return UserUsecase(user_methods=UserMethods(Repository()))


class UserController(Controller):
    dependencies = {
        "usecase": Provide(provide_user_usecase),
    }
    @post(dto=UserCreateDTO)
    async def create(self, data: UserModel, usecase: UserUsecaseProtocol) -> UUID:
        return await usecase.create(data=data)

    @patch(dto=UserUpdateDTO)
    async def update(self, data: UserModel, usecase: UserUsecaseProtocol) -> None:
        await usecase.update(data=data)

    @get(return_dto=UserReadDTO)
    async def get(self, usecase: UserUsecaseProtocol) -> UserModel:
        return await usecase.get(user_id=None)

    @delete()
    async def delete(self, usecase: UserUsecaseProtocol) -> None:
        await usecase.delete(user_id=None)
