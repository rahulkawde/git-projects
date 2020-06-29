# (*args)

def multiply_no(*arg):                  
    multiply= 1
    print(arg)
    for i in arg:
        multiply*= i
    return multiply

# num1 as parameter
def multiply_no1(num1,*arg):
    multiply= 1
    print(arg)
    for i in arg:
        multiply*= i
    return multiply

print(multiply_no(1,2,3))       
print(multiply_no1(1,2,3))   

num=[6,9,2]
print(multiply_no(*num))       # * for unpack 