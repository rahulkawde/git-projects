# odd even   using mod
def odd_even(l):
    odd_no =[]
    even_no =[]
    for i in l:
        if i % 2 ==0:              # using mod we find odd_even
            even_no.append(i)
        else:
            odd_no.append(i)               
    return [odd_no, even_no]            

    

n=[1,2,3,4,5,6,7,8,9,10]
print(odd_even(n))
