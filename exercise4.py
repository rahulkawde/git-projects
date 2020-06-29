# ask user name and char and show length and char count
user_name,char = input("enter your name char comma sepreted: ").split(",")
length = len(user_name)
count = (user_name.count(char))
print(f"length of your name is {length}") 
print(f"character count is {count}")
 
 
 #other method
#user_name,char = input("enter your name char comma sepreted: ").split(",")
#length = len(user_name)
#count = int(user_name.count(char))
#print(f"length of your name is {length} and character count is {user_name.lower().count(char.lower())}")
