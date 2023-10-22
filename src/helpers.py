from typing import Iterable, TypeVar


T = TypeVar("T")


def flatten(two_d_iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    return (item for row in two_d_iterable for item in row)


allowed_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
