from functools import wraps


def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        int_value = []
        for arg in args:
            int_value.append(type(arg) == int)
        if all(int_value):
            return function(*args, **kwargs)

        print("Invalid Arguments")

    return wrapper


@only_int_allow
def add_all_int_value(*args):
    total = 0
    for i in args:
        total += i
    print(total)


add_all_int_value(1, 2, 3, 4, 5, 'dd')
add_all_int_value(1, 2, 3, 4, 5)
