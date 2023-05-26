from functools import wraps


def singleton(cls):
    """Class decorator that allows to create only one class' instance."""
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.instance is None:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
