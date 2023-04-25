import logging
from typing import Callable, Any
from functools import wraps
from time import perf_counter


CallableToObject = Callable[..., object]

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s — %(levelname)-8s — %(message)s')
def log(level: int) -> Callable:
    def decorator(obj: CallableToObject) -> CallableToObject:
        @wraps(obj)
        def wrapper(*args: Any, **kwargs: Any) -> object:
            if isinstance(obj, type):
                instance: object = obj(*args, **kwargs)
                logging.log(level, f'Instantiated {obj.__name__}({args}, {kwargs})')
                return instance
            else:
                start:   float = perf_counter()
                result: object = obj(*args, **kwargs)
                finish:  float = perf_counter()
                time:    float = finish - start
                logging.log(level, f'Called {obj.__name__}({args}, {kwargs}), '
                            f'took {time:.1g} seconds, returned: {result}.')
                return result
        return wrapper
    return decorator

@log(logging.DEBUG)
def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    multiply(2, 3)
