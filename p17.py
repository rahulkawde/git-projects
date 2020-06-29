# input = [ 3,5,23,68,564]
# output = [3,5,33,77,565]√



def next_palindrome(n):
    n = n + 1
    while not is_palindrome(n):
        n +=1
    return n    

def is_palindrome(n):
    return str(n)== str(n)[::-1]    

def check(n):
    if n > 10:
        return next_palindrome(n)
    else:
        return n        


n = int(input('enter the number of test case '))
numbers = []
for i in range(n):
    num = int(input('Enter the number'))
    numbers.append(num)
for i in range(n):
    print (f'{numbers[i]} of palindrome is{check(numbers[i])}\n')    