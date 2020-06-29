# calculate time 
#  import time
# t1= time.time()
# t2= time.time()
# print(t2-t1)

from functools import wraps    # import use before def func.     
import time                 # for cal time
def time_cal(any_func):
    @wraps(any_func)
    def wrapper(*arg,** kwarg):
        t1=time.time()
        returned_val= any_func(*arg,**kwarg)    # use variable to store value
        t2=time.time()
        print(f'this function took {t2-t1} second.')
        return returned_val
    return wrapper    
       

@time_cal
def add(a,b):
    return a+b

@time_cal
def square(n):
    return[i**2 for i in (1,n+1)]

print( f'you using {add.__name__} function.')   
print(add.__doc__)
print(add(5,9)) 
print(square(8)) 



