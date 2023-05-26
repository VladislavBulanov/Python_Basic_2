from collections.abc import Callable
from functools import wraps


def how_are_you(func: Callable) -> Callable:
    """Decorator, asking how are you before function performing."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)

    return wrapper


@how_are_you
def test_function() -> None:
    """Test function."""
    print('<Тут что-то происходит...>')


test_function()
