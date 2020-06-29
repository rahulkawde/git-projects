def func(l,**kwarg):                 
    if kwarg.get('reverse_str')== True:         # get for access
        return [name[: : -1].title() for name in l]    # for reverse_str
    return[name.title() for name in l]                 #  for only l

n=('rahul', 'sachin', 'ganesh') 
print(func(n))     
print(func(n,reverse_str = True))