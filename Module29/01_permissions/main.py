from typing import Callable
from functools import wraps


USER_PERMISSIONS = ['admin']


def check_permission(user: str) -> Callable:
    """
    Decorator checking user's permission.
    :param user: user's account
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if user in USER_PERMISSIONS:
                return func(*args, **kwargs)
            raise PermissionError(
                'У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(
                    wrapper.__name__,
                )
            )
        return wrapper
    return decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
