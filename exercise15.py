#create a function and use in program 
def greter(a,b):
    if a > b:
        return a
    else:
       return b

num1 =int(input("enter a number:"))    
num2 =int(input("enter a number:"))    
bigger=greter(num1,num2)
print(f"{bigger} is greater.")