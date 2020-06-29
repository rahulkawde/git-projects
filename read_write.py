#read and convert
with open ('file.txt','r') as rf:
    with open ('file1.txt', 'a') as wf:  # for append
        for line in rf.readlines():     # for read line by line 
            name,salary = line.split(',')  # for separate
            wf.write(f'{name}\'s salary is {salary}')




