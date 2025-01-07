from dataclasses import dataclass, field
from uuid import UUID, uuid4

from models.values import Username, Email, Phone, Password


@dataclass()
class User:
    id: UUID = field(default_factory=uuid4)
    username: str = field(default=Username(), repr=False)
    email: str = field(default=Email(), repr=False)
    phone: str = field(default=Phone(), repr=False)
    password: str = field(default=Password(), repr=False)

