from collections.abc import Callable
from functools import wraps


def counter(func: Callable) -> Callable:
    """
    Decorator counting and printing how
    much times the function was called.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.count += 1
        print('Функция {func} была вызвана {count} раз(а).'.format(
            func=func.__name__,
            count=wrapper.count
        ))
        return result

    wrapper.count = 0
    return wrapper


@counter
def test_function() -> None:
    """Test function."""
    print('<Something happens...>')


for _ in range(4):
    test_function()
