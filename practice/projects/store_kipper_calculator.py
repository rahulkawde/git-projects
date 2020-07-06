# shop keeper calculator 
sum = 0            # for give a total
while (True):       # for continue ask
    user_input = input('Enter your item price amount or q for Quit:\n')
    if user_input != 'q':   # when enter no.
        sum = sum+ int(user_input)
    else:                   # when enter q
        print (f'Your total amount is {sum}')
        print( 'thank you for shop')   
        break               # for quit 