from collections.abc import Callable
from functools import wraps
from datetime import datetime


def logging(func: Callable) -> Callable:
    """Decorator logging function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('\nВыполняется функция <{}>.'.format(func.__name__))
        print('Документация функции:\n{}'.format(func.__doc__))
        try:
            result = func(*args, **kwargs)
            return result
        except BaseException as error:
            error_datatime = datetime.now()
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write('{date}\t<{func_name}>\t{error}\n'.format(
                    date=error_datatime,
                    func_name=func.__name__,
                    error=error
                ))
            print('Произошла ошибка <{}>'.format(error))

    return wrapper


@logging
def calculate_sum(num_1: int, num_2: int) -> int:
    """
    Function sums two specified numbers.
    """
    return num_1 + num_2


@logging
def divide_numbers(num_1: int, num_2: int) -> float:
    """
    Function divides first number by second number.
    :raise ZeroDivisionError: if second number is zero
    """
    return num_1 / num_2


@logging
def calculate_difference(num_1: int, num_2: int) -> int:
    """
    Function returns difference between two numbers.
    """
    return num_1 - num_2


number_1, number_2 = map(int, input(
    'Введите два целых числа через пробел: '
).split())
print(calculate_sum(number_1, number_2))
print(divide_numbers(number_1, number_2))
print(calculate_difference(number_1, number_2))
