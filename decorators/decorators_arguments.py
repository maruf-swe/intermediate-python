def decorator_func(any_func):
    def wrapper(*args, **kwargs):
        print("Started Decorators")
        return any_func(*args, **kwargs)

    return wrapper


# this is proper way & this called Syntactic Sugar
@decorator_func
def func(a):
    print(f"This is going to decorators function with arguments {a}")


func(7)


@decorator_func
def func2(a, b):
    print(a + b)


func2(2, 3)
