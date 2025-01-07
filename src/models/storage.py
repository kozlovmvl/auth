from typing import Any, Iterable, Protocol


class RepoProtocol(Protocol):
    async def get(self, **kwargs) -> Any:
        ...

    async def list(self, **kwargs) -> Iterable:
        ...

    async def save(self, obj: Any):
        ...

    async def delete(self, obj: Any):
        ...
