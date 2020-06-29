# Dictwriter:     giv a dict
from csv import DictWriter
with open ('file3.csv','w',newline='')  as wf:   # w create file also
    csv_writer = DictWriter(wf,fieldnames=['name','country']) 
    # we add fieldname for header
    csv_writer.writeheader()
# 2 method   writerow, writerows
#writerow
    # csv_writer.writerow({
    # 'name': 'rahul',
    # 'country' : 'INDIA'
    # })
    # csv_writer.writerow({
    # 'name': 'sachin',
    # 'country' : 'INDIA'
    # })
#writerows
    csv_writer.writerows([
        {'name':'rahul','country':'India'},
        {'name':'sachin','country':'India'},
        {'name':'rajesh','country':'India'}
            ])      