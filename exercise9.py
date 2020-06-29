# enter name and char count 
# r: 1
# a: 2.....
name = input("enter your name: ")
#rahul kawde    length = 11
#0123456789     intex
#output
#r : 1  name[0]:name.count(name[0])
temp_ver = ""     # store for blank char
i = 0
while i < len(name):
    if name [i] not in temp_ver :     # temp_ver for double char
     temp_ver += name[i]  # add double char in temp_ver 
     print(f"{name[i]} : {name.count(name[i])}")
    i +=1 # dont forgot increasing i value
