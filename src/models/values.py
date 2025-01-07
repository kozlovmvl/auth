from main import settings
from models.exceptions import (
    UsernameValidationError,
    EmailValidationError,
    PhoneValidationError,
    PasswordValidationError,
)
from models.utils import make_hash


class BaseField:
    def __set_name__(self, owner, name):
        self.field_name = "_" + name

    def __get__(self, obj, objtype=None) -> str:
        return getattr(obj, self.field_name)

    def __set__(self, obj, value: str) -> None:
        if value is self:
            setattr(obj, self.field_name, None)
        else:
            self._validate(value)
            setattr(obj, self.field_name, value)

    def _validate(self, value: str):
        raise NotImplementedError


class Username(BaseField):
    def _validate(self, value: str):
        if len(value) < settings.USERNAME_MIN_LENGTH:
            raise UsernameValidationError


class Email(BaseField):
    def _validate(self, value: str):
        parts = value.split("@")
        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            raise EmailValidationError


class Phone(BaseField):
    def _validate(self, value: str):
        if len(value) != settings.PHONE_LENGTH:
            raise PhoneValidationError


class Password(BaseField):
    def _validate(self, value: str):
        if len(value) < settings.PASSWORD_MIN_LENGTH:
            raise PasswordValidationError

    def __set__(self, obj, value: str) -> None:
        if value is self:
            setattr(obj, self.field_name, None)
        else:
            self._validate(value)
            setattr(obj, self.field_name, make_hash(value))
