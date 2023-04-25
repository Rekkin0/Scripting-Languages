from typing import TypeVar, Callable, Iterable

from utils import return_except


T = TypeVar('T')

@return_except()
def forall(predicate: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    """
    Returns True if all elements in the iterable satisfy the predicate.
    """
    return all(predicate(element) for element in iterable)

@return_except()
def exists(predicate: Callable[[T], bool], iterable: Iterable[T]) -> bool:
    """
    Returns True if at least one element in the iterable satisfies the predicate.
    """
    return any(predicate(element) for element in iterable)
   
@return_except() 
def atleast(predicate: Callable[[T], bool], iterable: Iterable[T], bound: int) -> bool:
    """
    Returns True if at least n elements in the iterable satisfy the predicate.
    """
    return bound <= sum(1 for element in iterable if predicate(element))

@return_except()
def atmost(predicate: Callable[[T], bool], iterable: Iterable[T], bound: int) -> bool:
    """
    Returns True if at most n elements in the iterable satisfy the predicate.
    """
    return bound >= sum(1 for element in iterable if predicate(element))


if __name__ == '__main__':
    print(forall(lambda x: x > 0, iterable=[1, 2, 3]))
    print(forall(lambda x: x > 0, iterable=[1, -2, 3]))
    # print(forall(1))
    print()
    print(exists(lambda x: x > 0, iterable=[1, -2, 3]))
    print(exists(lambda x: x > 0, iterable=[-1, -2, -3]))
    # print(exists(1))
    print()
    print(atleast(lambda x: x > 0, iterable=[1, -2, 3], bound=2))
    print(atleast(lambda x: x > 0, iterable=[1, -2, -3], bound=2))
    # print(atleast(1))
    print()
    print(atmost(lambda x: x > 0, iterable=[1, -2, 3], bound=2))
    print(atmost(lambda x: x > 0, iterable=[1, 2, 3], bound=2))
    # print(atmost(1))
    ...
