num= [1,2,3,4,5,6,7,8,9,10]
# o/p = [-1,4,-3,8,-5,12,-8,-9,20]

num_list =[]
for i in num:
    if i%2==0:
        num_list.append(i*2)
    else:
        num_list.append(-i)             #old version
        
print(num_list)
  

num_list2 = [i*2 if (i%2==0) else (-i) for i in num ]     # new version
print(num_list2)