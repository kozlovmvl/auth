from litestar.dto import DataclassDTO
from litestar.dto.config import DTOConfig

from models.entities import User


type UserModel = User


class UserReadDTO(DataclassDTO[UserModel]):
    config = DTOConfig(exclude={"password"})
    

class UserCreateDTO(DataclassDTO[UserModel]):
    config = DTOConfig(exclude={"id"})


class UserUpdateDTO(DataclassDTO[UserModel]):
    config = DTOConfig(exclude={"id", "username"})
