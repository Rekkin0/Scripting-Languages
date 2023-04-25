from typing import Optional, Generator
from functools import cache
import logging

from exc4 import Function, Generator, make_generator, print_generator
from exc6 import log


mem_function: Optional[tuple[Function, ...]] = None
def make_mem_generator(function: Function) -> Generator:
    """
    Returns a generator that yields the memoized results of a function.
    """
    global mem_function
    if mem_function is None or mem_function[0] is not function:
        mem_function = function, cache(function)
    return make_generator(mem_function[1])

@log(logging.DEBUG)
def print_generator_timed(generator: Generator, count: int) -> None:
    print_generator(generator, count)


if __name__ == '__main__':
    from exc4 import fibonacci
    
    print_generator_timed(make_mem_generator(fibonacci), 35)
    print('\n')
    print_generator_timed(make_mem_generator(fibonacci), 35)
    ...
