import pytest
from models.entities import User
from web.usecases import UserUsecase


@pytest.mark.asyncio
async def test_user_usecase(mock_user_methods):
    usecase = UserUsecase(user_methods=mock_user_methods)
    user = User(username="username", email="name@host")
    await usecase.create(data=user)
    await usecase.get(user_id=user.id)
    await usecase.update(data=user)
    await usecase.delete(user_id=user.id)
    assert user
