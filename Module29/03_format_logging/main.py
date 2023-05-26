from typing import Callable
from functools import wraps
from datetime import datetime
from time import time


def timer(cls, func: Callable, date_format: str) -> Callable:
    """
    Decorator describes start time of the function
    and time of function's performing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_format = date_format
        for symbol in result_format:
            if symbol.isalpha():
                result_format = result_format.replace(symbol, '%' + symbol)

        print('- Запускается "{}.{}". Дата и время запуска: {}'.format(
                cls.__name__,
                func.__name__,
                datetime.now().strftime(result_format),
        ))

        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()

        print('- Завершение "{}.{}", время работы = {} сек.'.format(
            cls.__name__,
            func.__name__,
            round(end_time - start_time, 3),
        ))
        return result
    return wrapper


def log_methods(date_format: str):
    """Class decorator logging all class' methods (exclude magic methods)."""
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                decorated_method = timer(cls, current_method, date_format)
                setattr(cls, method, decorated_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
