from typing import Iterable
from models.entities import User


class Repository:
    async def get(self, **kwargs) -> User:
        ...

    async def list(self, **kwargs) -> Iterable[User]:
        ...

    async def save(self, obj: User):
        ...

    async def delete(self, obj: User):
        ...
