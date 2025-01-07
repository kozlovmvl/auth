from typing import Protocol

from api.auth.dto import Credentials
from models.methods import UserMethodsProtocol
from models.utils import make_hash


class TokenUsecaseProtocol(Protocol):
    async def create(self, credentials: Credentials) -> str:
        ...

    async def delete(self, token: str) -> None:
        ...


class TokenUsecase:
    def __init__(self, user_methods: UserMethodsProtocol):
        self.user_methods = user_methods

    async def create(self, credentials: Credentials) -> str:
        user = await self.user_methods.get(username=credentials.username, password=make_hash(credentials.password))

    async def delete(self, token: str) -> None:
        ...
