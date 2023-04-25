from typing import Callable, Generator


Function = Callable[[int], int]
Generator = Generator[int, None, None]

def make_generator(function: Function) -> Generator:
    """
    Returns a generator that yields the results of a function.
    """
    n: int = 1
    while True:
        yield function(n)
        n += 1
        
def print_generator(generator: Generator, count: int) -> None:
    for _ in range(count):
        print(next(generator), end=', ')
    print('...\n')

def fibonacci(n: int) -> int:
    """
    Returns the n-th Fibonacci number (recursively).
    """
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iter(n: int) -> int:
    """
    Returns the n-th Fibonacci number (iteratively).
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    
    return a


if __name__ == '__main__':
    fib_gen = make_generator(fibonacci)
    print('Fibonacci sequence')
    print_generator(fib_gen, 15)
    
    a1: int = 10
    r:  int = 4
    arth_gen = make_generator(lambda n: a1 + (n-1)*r)
    print('Arithmetic sequence — 10+(n-1)*4')
    print_generator(arth_gen, 15)
        
    a1: int = 2
    q:  int = -2
    geom_gen = make_generator(lambda n: a1 * q**(n-1))
    print('Geometric sequence — 2*(-2)^(n-1)')
    print_generator(geom_gen, 15) 
    ...
