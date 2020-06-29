# cube function n create dic
def cube_fuc(n):
   cubes={}
   for i in range(1,n+1):    #from 1 to n no.
       cubes[i]= i**3         # for key and value
   return cubes     


print(cube_fuc(5))          


