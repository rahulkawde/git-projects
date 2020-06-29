l=['abc', 'xyz', 'lmn']

# def reverse_str(l):
#     number=[]
#     for i in l:
#         number.append(i[: : -1])       # old version
#     return number

def reverse_str(l):
     return[i[: : -1] for i in l]   # use list compre

print(reverse_str(l))    