def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('donn\'t enter zero')
    except TypeError:
        print('plz enter number') 
    except:
        print('unexcepted error')

print(divide(1,8)) # without error
print(divide(1,0))  # ZeroDivisionError
print(divide(1,'8'))  #TypeError           

    