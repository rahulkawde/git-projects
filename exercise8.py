# additin of more than digit no.
# example 1234....
n= input("enter no more than one:")
length = len(n)
total = 0
i = 0
while i < len(n): # length give no.
     total += int(n[i]) # we do 1+2+3... int(n[i]) 
     i += 1
print(total)
