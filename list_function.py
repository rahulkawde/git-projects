numbers= list(range(1,11))   # make a list using range function
#print(numbers)

def negative_number(l):
    negative= []
    for i in l:
        negative.append(-i)
    return negative


print(negative_number(numbers))        