from functools import wraps

def only_int_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            int_value = []
            for arg in args:
                int_value.append(type(arg) == data_type)
            if all(int_value):
                return function(*args, **kwargs)

            print("Invalid Arguments")

        return wrapper
    return decorator

@only_int_data_type_allow(int)
def add_all_int_value(*args):
    total = 0
    for i in args:
        total += i
    print(total)


add_all_int_value(1, 2, 3, 4, 5, 'dd')
add_all_int_value(1, 2, 3, 4, 5)