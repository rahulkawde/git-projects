given = (input('Enter your list'))
given = list(given)
# given = [1,2,3]
print(given[::-1])# silcing2

reverse1 = given[:]  # build fuction reversed
reverse1.reverse()
print(reverse1)

for i in range(len(given)//2):
    given[i],given[len(given) -i -1] = given[len(given) -i -1],given[i]
    # print(f'{i}   ,  {given}')
print(given)