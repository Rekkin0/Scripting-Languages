import logging
from typing import ParamSpec, TypeVar, Callable
from functools import wraps


P = ParamSpec('P')
R = TypeVar('R')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s — %(levelname)-8s — %(message)s')
def log(level: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Decorator that logs a class being instantiated or a function 
    being called (the time it took to call it and its return value).
    """
    def decorator(obj: Callable[P, R]) -> Callable[P, R]:
        @wraps(obj)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            if isinstance(obj, type):
                instance: R = obj(*args, **kwargs)
                logging.log(level, f'Instantiated {obj.__name__}({args}, {kwargs})')
                return instance
            else:
                from time import perf_counter
                start: float = perf_counter()
                result:    R = obj(*args, **kwargs)
                time:  float = perf_counter() - start
                logging.log(level, f'Called {obj.__name__}({args}, {kwargs}), '
                            f'took {time:.2g} seconds, returned: {result}.')
                return result
        return wrapper
    return decorator

@log(logging.DEBUG)
def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    multiply(2, 3)
