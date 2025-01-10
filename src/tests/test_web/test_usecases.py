import uuid
import pytest
from api.auth.dto import Credentials
from api.users.usecases import UserUsecase
from api.auth.usecases import TokenUsecase
from models.entities import Token, User


@pytest.mark.asyncio
async def test_user_usecase(mock_user_methods):
    usecase = UserUsecase(user_methods=mock_user_methods)
    user = User(username="username", email="name@host")
    await usecase.create(data=user)
    await usecase.get(user_id=user.id)
    await usecase.update(data=user)
    await usecase.delete(user_id=user.id)
    assert user


@pytest.mark.asyncio
async def test_token_usecase(mock_token_methods, mock_user_methods):
    user = User(username="username", email="name@host")
    await mock_user_methods.save(user)
    usecase = TokenUsecase(token_methods=mock_token_methods, user_methods=mock_user_methods)
    token = Token(user_id=user.id)
    await usecase.create(credentials=Credentials(username="username", password="password"))
    await usecase.delete(jwt=token.jwt)
    assert token
