
#modify number guessing game
winning_number = 99 
guess = 1 # for we write which time user guess no.
number = int(input("enter your no between 1 to 100:"))  # user no
game_over = False #bcz game start here
while not game_over:    #while bcz of we want compare no
     if number ==winning_number:
         print(f"YOU WIN!!! and you guess in {guess} time")
         game_over = True # user win game i.e game_over true
     else:
        #if number >  winning_number:
          #  print("too high")
         #   guess +=1    # we add guess by 1 
         #   number = int(input("try again"))  #give an another chance
       # else:
           # print("too low")
           # guess +=1  # we geuss add by 1
          #  number = int(input("try again")) # give an another chance


            #DRY
            if number >  winning_number:
                print("too high")
            else:                        # we use dry 
                print("too low")
            guess +=1  # we geuss add by 1
            number = int(input("try again"))

    