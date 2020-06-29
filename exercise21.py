#comman no in two list
[1,2,3,4,5,6,7,8,9],[2,4,3,7,22,44,55,1,9]

#output = [2,4,3,7,1,9]
 
def comman_fac(l1, l2):
    comman = []
    for i in l1:    # 1st loop for l1
        if i in l2: # check in l2
            comman.append(i)
    return comman

print(comman_fac([1,2,3,4,5,6,7,8,9],[2,4,3,7,22,44,55,1,9]))


        
     