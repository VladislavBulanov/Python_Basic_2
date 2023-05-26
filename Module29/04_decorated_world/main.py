from typing import Callable
from functools import wraps


def decorator_with_args_for_any_decorator(decorator_to_modify: Callable) -> Callable:
    def decorator(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_modify(func, *args, **kwargs)
        return decorator_wrapper
    return decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *dec_args, **dec_kwargs) -> Callable:
    """Sample of decorator."""
    @wraps(func)
    def wrapper(*func_args, **func_kwargs) -> Callable:
        print('Переданные арги и кварги в декоратор:', dec_args, dec_kwargs)
        return func(*func_args, **func_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    """Sample of decorated function."""
    print("Привет,", text, num)


decorated_function("Юзер", 101)
