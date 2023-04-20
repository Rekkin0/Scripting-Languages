from typing import Callable, Iterable, TypeVar


T = TypeVar('T')

def forall(predicate: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    for element in iterable:
        if not predicate(element):
            return False
    return True
    # return False not in (predicate(element) for element in iterable)

def exists(predicate: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    for element in iterable:
        if predicate(element):
            return True
    return False
    # return True in (predicate(element) for element in iterable)
    
def atleast(n: int, predicate: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    return sum(1 for element in iterable if predicate(element)) >= n

def atmost(n: int, predicate: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    return sum(1 for element in iterable if predicate(element)) <= n