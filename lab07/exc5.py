from typing import Optional, Generator
from functools import cache, _lru_cache_wrapper

from exc4 import Function, Generator, make_generator, print_generator, fibonacci


mem_function: Optional[tuple[Function, _lru_cache_wrapper[int]]] = None
def make_mem_generator(function: Function) -> Generator:
    """
    Returns a generator that yields the memoized results of a function.
    """
    global mem_function
    if mem_function is None or mem_function[0] is not function:
        mem_function = function, cache(function)
    return make_generator(mem_function[1])


if __name__ == '__main__':
    print('Fibonacci sequence')
    print_generator(make_mem_generator(fibonacci), 35)
    
    print('Fibonacci sequence')
    print_generator(make_mem_generator(fibonacci), 35)
    
    print('Squares')
    print_generator(make_mem_generator(lambda x: x**2), 35)
