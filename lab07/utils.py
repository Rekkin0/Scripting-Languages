from typing import ParamSpec, TypeVar, Callable


P = ParamSpec('P')
R = TypeVar('R')
    
def return_except(except_msg: str = 'Something went wrong — check your input.',
                  ) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(function: Callable[P, R]) -> Callable[P, R]:
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                return function(*args, **kwargs)
            except:
                raise SystemExit(except_msg)
        return wrapper
    return decorator