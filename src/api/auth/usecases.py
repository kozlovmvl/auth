from typing import Protocol

from api.auth.dto import Credentials
from models.methods import UserMethodsProtocol, TokenMethodsProtocol
from models.utils import make_hash
from models.entities import Token


class TokenUsecaseProtocol(Protocol):
    async def create(self, credentials: Credentials) -> str:
        ...

    async def delete(self, token: str) -> None:
        ...


class TokenUsecase:
    def __init__(self, token_methods: TokenMethodsProtocol, user_methods: UserMethodsProtocol):
        self.token_methods = token_methods
        self.user_methods = user_methods

    async def create(self, credentials: Credentials) -> str:
        user = await self.user_methods.get(
            username=credentials.username, 
            password=make_hash(credentials.password),
        )
        token = Token(user_id=user.id)
        await self.token_methods.save(token) 
        return token.jwt

    async def delete(self, jwt: str) -> None:
        token = await self.token_methods.get(jwt=jwt) 
        await self.token_methods.delete(token)
