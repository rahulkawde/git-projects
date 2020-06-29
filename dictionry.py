user_info={ "name ": "rahul",
"age": 23,
"movie": "marvel"}
print(type(user_info))

#user_info = user_info.items()
#print(user_info)


for key, value in user_info.items():
    print(f"key is {key} and value is {value} ")