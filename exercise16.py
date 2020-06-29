#find gretest number                            
def gretest(a,b,c):                             
    if  a>b and a>c:      # use and not or
        return a
    elif b>a  and b>c:
        return b    
    else:
        return c

num1 =int(input("enter a number:"))    
num2 =int(input("enter a number:")) 
num3 =int(input("enter a number:"))   
bigger=gretest(num1,num2,num3)
print(f"{bigger} is greatest.")                