# decrator2     __doc__
from functools import wraps
def print_func(any_func):
    @wraps(any_func)
    def wrapper(*arg,** kwarg):
        print (f" you are calling {any_func.__name__} function.")
        print(f"{any_func.__doc__}")
        return any_func(*arg,** kwarg)
    return wrapper    

@print_func
def add(a,b):
    ''' this is function using for add a no,'''
    return a+b

print(add(4,2))    