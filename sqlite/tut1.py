import sqlite3

conn = sqlite3.connect('database.db')
print('success')
# create table:
# command = 'create table todo (id text , task int, date text, status text)'
# conn.execute(command)   # make table from command variable

# # insert value in table:
# insert = "insert into todo (id,task, date, status) values ('rahul',1,'20-07-2020','not done')"
# insert = "insert into todo (id,task, date, status) values ('sachin',2,'24-07-2020','not done')"
# conn.execute(insert)   # make table from insert variable
# conn.commit()       # commit the table

# # retrive data form data:
# retrive_data = 'select * from todo'
# result = conn.execute(retrive_data)
# # method 1:
# for row in result:    # we get tuple form data 
#     id,task,date,status = row
#     print(id,task,date,status)
# output:  rahul 1 20-07-2020 not done
#          sachin 2 24-07-2020 not done    

# method 2: using fatch:
# R= result.fetchall()  # for all data
# print(R)
# output: [('rahul', 1, '20-07-2020', 'not done'), ('sachin', 2, '24-07-2020', 'not done')]


# # update table:
# update1 = "update todo set status = 'done' where id = 'rahul'"
# update2 = "update todo set status = 'done' where id = 'sachin'"

# conn.execute(update1)
# conn.execute(update2)

# conn.commit()
# print('total change:',conn.total_changes)
# result = conn.execute('select * from todo')
# for row in result:
#     print(row)


#delete table:
delete = "delete from todo where id = 'rahul'"
conn.execute(delete)
conn.commit()
print('total change:',conn.total_changes)
result = conn.execute('select * from todo')
for row in result:
    print(row)
# we delete 1st row in table
# and delete all table :
