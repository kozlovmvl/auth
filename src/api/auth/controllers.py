from litestar import Controller, post, delete
from litestar.di import Provide

from api.auth.dto import Credentials, CredentialsDTO
from api.auth.usecases import TokenUsecaseProtocol, TokenUsecase


async def provide_token_usecase() -> TokenUsecaseProtocol:
    return TokenUsecase()


class TokenController(Controller):
    dependencies = {
        "usecase": Provide(provide_token_usecase),
    }
    @post(dto=CredentialsDTO)
    async def create(self, credentials: Credentials, usecase: TokenUsecaseProtocol) -> str:
        return await usecase.create(credentials=credentials)

    @delete()
    async def delete(self, usecase: TokenUsecaseProtocol) -> None:
        await usecase.delete(token="")
