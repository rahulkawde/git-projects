#  next palindrome

def next_palindrome(n):
    n = n + 1
    while not palindrome(n):
        n += 1
    return n    
    

def palindrome(n):
    return str(n)==str(n)[::-1]


n = int(input('enter the number of test case '))
numbers = []
for i in range(n):
    num = int(input('Enter the number'))
    numbers.append(num)
    
for i in range(n):
    print(f'{numbers[i]}     {next_palindrome(numbers[i])}')    