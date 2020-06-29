# # import subprocess

# # a= subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

# # a= [i.split(':')[1][1:-1]for i in a if 'all user profiles' in i]

# # for i in a:
# #     result = subprocess.check_output(['netsh','wlan','show','profies',i,'key=clear']).decode('utf-8').split('\n')
# #     result = [b.split(':'[1][1:-1])for b in result if 'key content' in b ]
# #     try:
# #         print('{:<30}|  {:<}'.format(i,result[0]))
# #     except IndexError:
# #         print('{:<30}|  {:<}'.format(i,''))

# # input('')        
    


# import subprocess

# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))
# input("")




# # def pattern(n):
# #     k= 2*n-2
# #     for i in range(0,n):
# #         for j in range(0,k):
# #             print('*',end='')
# #         k=k-1
# #         for j in range(0,i+1):
# #             print('*',end='')
# #         # print('\r')    
# #         print('&#g2r')    


# # pattern(5)\




# # import winsound
# # frequency = 2500
# # duration = 5000
# # winsound.beep(f,d)



# # import turtle
    
# # turtle.forward(50)    
# # turtle.left(90)
# # turtle.forward(50)    
# # turtle.left(90)
# # turtle.forward(50)    
# # turtle.left(90)
# # turtle.forward(50)    
# # turtle.left(90)



# row = 6
# k=2*row-2
# for i in range(row,-1,-1):
#     for j in range(k,0,-1):
#         print(end='')
#     k +=1
#     for j in range(0,i,-1):
#         print('*',end='')
#     print('')        

# triangle
n=9
for i in range(n):
    for j in range(i):
        print('*',end='')
    print('')    



