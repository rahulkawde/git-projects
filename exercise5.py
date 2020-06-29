# number guessing game
winning_number= 55
user_number= int(input("enter your number :"))
if user_number == winning_number:
    print("YOU WIN!!!")
elif user_number > winning_number:
    print("too high")
else:
    print("too low")