# task:
# print: you are calling (function) name
# print: this function takes two parameter and return theire sum
# value of sum
from functools import wraps


def decorator_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'You are calling {func.__name__} function')
        print(f'{func.__doc__}')
        return func(*args, **kwargs)

    return wrapper


@decorator_func
def add(a, b):
    '''this function takes two parameter and return their sum'''
    print(a + b)


add(5, 5)
