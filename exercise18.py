#fibonnaci series
# 0 1 1 2 3 5 8 .....
def fibonnaci(n):
     a=0
     b=1
     if n==1:
         print(a)
     elif n==2:
         print(a,b)  
     else :
         print(a,b,end=" ")
         for i in range(n -2 ): # n-2 bcz we already add 2 no.
             c = a+b            #0+1, 1+1, 2+1.....
             a = b              #1 ,1,2,3....
             b = c              #1,2,3,5....
             print(b, end = " ")

fibonnaci(10)           