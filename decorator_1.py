# decorator 1
from functools import wraps    # use import
def decorator_func(any_func):       # outer fuction   
    @wraps(any_func)      #  for doc
    def wrapper_func(*arg, **kwarg): # inner fuction
        '''this is doc'''           # add __doc__ 
        print("this is decor")       # decorator o/p
        return(any_func( *arg, **kwarg))  # for inner function
    return wrapper_func                 # o/p for decorator

@decorator_func             # @ is shortcut for decorator
def fuc1(a):
    '''this is fuc1'''
    return(f"this is {a}")

@decorator_func
def fuc2(a,b):
    return(a+b)


print(fuc2(2,3))
print(fuc1('r'))    

print(fuc1.__doc__) # o/p is   doc statement
print(fuc1.__name__) # o/p is wrapper_func