from typing import Iterable, TypeVar


T = TypeVar("T")


def flatten(two_d_iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    return (item for row in two_d_iterable for item in row)
