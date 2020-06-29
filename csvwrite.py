#writer dictWriter
#Writer :
from csv import writer
with open ('file2.csv','w',newline='')  as wf:   # w create file also
    csv_write = writer(wf)     # create object
# 2 method   writerow, writerows
#writerow
    # csv_write.writerow(['name','age']) # object.method([ '' ,''])
    # csv_write.writerow(['rahul','23'])
    # csv_write.writerow(['sachin','21'])
#writerows
    csv_write.writerows([['name','age'],['rahul','23'],['sachin','21'],['rajesh','50']])    




