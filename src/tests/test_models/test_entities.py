import pytest

from models.entities import User
from models.exceptions import (
    UsernameValidationError,
    EmailValidationError,
    PhoneValidationError,
    PasswordValidationError,
)


def test_valid_user():
    user = User(
        username="username",
        email="name@host",
        phone="+88888888888",
        password="password",
    )
    assert user


def test_invalid_user():
    user = User()
    with pytest.raises(UsernameValidationError):
        user.username = "1"
    with pytest.raises(EmailValidationError):
        user.email = "1"
    with pytest.raises(PhoneValidationError):
        user.phone = "1"
    with pytest.raises(PasswordValidationError):
        user.password = "1"
