# input (3,[1,2,3])
#output (1,8,27)

def xyz(num, *args):
    if args:   # only for args
        return [i ** num for i in args] #
    else:
        return " you didn't type args "

num =[1,2,3] 
s=(xyz(7,*num))          #don't forget to add * 
print (s)