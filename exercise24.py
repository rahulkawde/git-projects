user_info = {}
name= input('what is your name : ')
age = input('what is yor age : ')
movie= input('type your fav movie comma seperated : ').split(',')
song= input('type your fav song comma seperated :  ').split(',')

user_info['name'] = name
user_info['age'] =age
user_info['movie'] = movie
user_info['song'] =song
  

#print(user_info)       # for in strightline dic
for key,value in user_info.items():
    print(f"{key} : {value}")   # for vertical dic
