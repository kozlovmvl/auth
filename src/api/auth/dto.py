from dataclasses import dataclass

from litestar.dto import DataclassDTO


@dataclass()
class Credentials:
    username: str
    password: str


class CredentialsDTO(DataclassDTO[Credentials]):
    ...
