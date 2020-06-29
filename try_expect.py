# try except else finally
while True:       # for infinte loop
    try:
        age= int(input("enter your age : "))
                  
    except ValueError:          # known error
        print('enter integer not string')
    except :
        print('unknown error')  
    else:                      # else
        if age < 18:
            print('you cann\'t play game.')
        else:
            print('you can play.')  
            break               #for cut loop  
    finally:
        print('finally block here....')    
    
   