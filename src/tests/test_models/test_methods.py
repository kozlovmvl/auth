import uuid
import pytest

from models.entities import User, Token
from models.methods import UserMethods, TokenMethods


@pytest.mark.asyncio
async def test_user_methods(mock_user_repo):
    user_methods = UserMethods(repo=mock_user_repo)
    user_obj = User(username="username", email="name@host")
    await user_methods.save(user=user_obj)
    _ = await user_methods.get(id=user_obj.id)
    await user_methods.delete(user=user_obj)
    assert user_obj


@pytest.mark.asyncio
async def test_token_methods(mock_token_repo):
    token_methods = TokenMethods(repo=mock_token_repo)
    token_obj = Token(user_id=uuid.uuid4())
    await token_methods.save(token=token_obj)
    _ = token_methods.get(jwt=token_obj.jwt)
    await token_methods.delete(token=token_obj)
    assert token_obj 
