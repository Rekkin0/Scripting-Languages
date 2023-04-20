from typing import Callable, Generator


def make_generator(function: Callable[[int], int]) -> Callable[[], Generator[int, None, None]]:
    def generator():
        n = 1
        while True:
            yield function(n)
            n += 1
    return generator