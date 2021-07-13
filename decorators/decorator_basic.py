def decorator_func(any_func):
    def wrapper():
        print("Started")
        any_func()
        print("Ended")

    return wrapper


# this is proper way & this called Syntactic Sugar
@decorator_func
def func():
    print("Maruf is cool Boy")


def func2():
    print("please stop")


func()
# another way to call decorator 
x = decorator_func(func2)
x()
