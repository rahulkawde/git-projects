# factorial no.

5!= 5*4*3*2*1

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number *factorial(number - 1) # using recursion   


    
def zeroTrailingFactorial(number):
    count= 0 
    i = 5
    # 100! = 100//5+100//5*5 ==== 20+4====24  logic
    while(number//i!=0) :
        # print(factorial(number)) 
        count += int(number/i)
        i=i*5
    return count    

number = int(input('Enter the number:\n'))
print (zeroTrailingFactorial(number))
# print(factorial(number)) 
