def even(n):
    for i in range(1,n+1):  # range(2,n+1,2):
        if i%2==0:          #   yield i
            yield i

for i in even(7):
    print(i)            # loop for print