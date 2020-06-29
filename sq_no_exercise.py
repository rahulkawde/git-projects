#n= int(input("enter your no.:"))
#n= list(range(n))
def square_no(l):
    square=[]         # use for store 
    for i in l:
        square.append(i**2)
    return(square)    


n= list(range(1,11))
print(square_no(n))    


