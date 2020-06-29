#using for loop 
# enter name and char count 
# r: 1 
# a: 2.....
name=input("enter your name:")
#rahul kawde    length = 11
#0123456789     intex
#output
#r : 1  name[0]:name.count(name[0])
temp_ver= ""    # for double char
for i in range(len(name)):
    if name[i] not in temp_ver:
        print(f"{name[i]}:{name.count(name[i])}") #1st loop finish
        temp_ver+= name[i]