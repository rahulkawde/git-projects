# decorator with agrument

from functools import wraps 
def type_fun(data_type):                    #decorator
    def decorator(function):                #function
        @wraps(function)
        def wrapper(*arg,**kwarg):          #wrapper
            if all([type(i)== data_type for i in arg]):
                return function(*arg,**kwarg)
            print("invalid function")
        return wrapper 
    return decorator

@type_fun(str)
def string_join(*arg):
    string= " "
    for i in arg:
        string += i
    return string

print(string_join("rahul","kawde"))              
