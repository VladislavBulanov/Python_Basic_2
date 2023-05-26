from collections.abc import Callable
from functools import wraps
from time import sleep


def slowdown_function(func: Callable) -> Callable:
    """Decorator slowing down function performing."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print('Please wait...')
        sleep(3)
        result = func(*args, **kwargs)
        return result

    return wrapper


@slowdown_function
def some_function() -> str:
    """Test function returning some string."""
    print('<Function performing...>')
    return 'Some result'


print(some_function())
