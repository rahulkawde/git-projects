#def reverse_list(l):
#    return l[: :-1]

   
# using pop n append
def reverse_list(l):
    reverse=[]
    for i in range(len(l)):
        poped_item= l.pop()      # for reverse
        reverse.append(poped_item)
    return reverse    


n= [1,2,3,4]    
print(reverse_list(n)) 