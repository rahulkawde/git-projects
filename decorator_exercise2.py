from functools import wraps
def only_int(function):
    @wraps(function)
    def wrapper(*arg,**kwarg):
        if all([type(i)== int for i in arg]):             #if check type of function
            return function(*arg,**kwarg)                  # all use to check 
        print('invaild argument')                   #else
    return wrapper    

@only_int
def add(*args):
    total=[]
    for i in args:
        total += i
    return total

 
print(add(1,2,3))