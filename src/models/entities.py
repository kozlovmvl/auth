from dataclasses import dataclass, field
from uuid import UUID, uuid4

from models.values import Username, Email, Phone, Password, DateExpire, JWT


@dataclass()
class User:
    id: UUID = field(default_factory=uuid4)
    username: str = field(default=Username(), repr=False)
    email: str = field(default=Email(), repr=False)
    phone: str = field(default=Phone(), repr=False)
    password: str = field(default=Password(), repr=False)


@dataclass()
class Token:
    user_id: UUID
    date_expire: float = field(default=DateExpire(), repr=False)
    jwt: str = field(default=JWT(), repr=False)

    def as_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "date_expire": self.date_expire,
        }
