# num= list(range(1,11))

# even_no=[i for i in num if i%2==0]
# odd_no=[i for i in num if i%2!=0]

# print(even_no)
# print(odd_no)

# def number_t(l):
#     number=[]
#     for i in l:
#         if type(i)== int or type(i)== float:
#             number.apppend(i)
#         return number


def number_t1(l):
    return[str(i) for i in l if (type(i)== int or type(i)== float)]

# print(number_t ([True,False,1,2,3.8]))    
print(number_t1 ([True,False,1,2,3.8])) 