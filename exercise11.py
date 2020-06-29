# using for loop addition of guess no:
#123
# # n[0]------> 1
# n[1]----> 2
#n[2]-----> 3
#total = n[i]
n= input("enter your numbers:")
total=0
for i in range(0,len(n)):
    total += int(n[i])

print(total)