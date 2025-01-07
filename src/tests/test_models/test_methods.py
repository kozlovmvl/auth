import pytest

from models.entities import User
from models.methods import UserMethods


@pytest.mark.asyncio
async def test_user_methods(mock_repo):
    user_methods = UserMethods(repo=mock_repo)
    user_obj = User(username="username", email="name@host")
    await user_methods.save(user=user_obj)
    _ = await user_methods.get(id=user_obj.id)
    await user_methods.delete(user=user_obj)
    assert user_obj
