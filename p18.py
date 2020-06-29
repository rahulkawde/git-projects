# multi player number guessing game:

import random
# n = [for i in range(1,101)] 
winning_number = random.randint(1,100) # for random number
guess = 1
number = int(input('Enter your number between 1 to 100 : \n'))
game_over = False

while not  game_over :
    if winning_number==number:
        print(f'You win and you guess in {guess} time ')
        game_over = True
    else:
        if number >  winning_number:
           print("too high")
           guess +=1    # we add guess by 1 
           number = int(input("try again"))  #give an another chance
        else:
            print("too low")
            guess +=1  # we geuss add by 1
            number = int(input("try again")) # give an another chance

            # if number > winning_number:
            #     print('too high')
            # else:
            #     print('too low') 
            #     guess =+1
            #     number=int(input('Try again'))

       


