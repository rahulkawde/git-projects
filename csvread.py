# reader dictreader
# using reader
from csv import reader   # csv = module
with open ('file.csv','r') as rf:
    csv_reader = reader(rf)
    #iterator
    next (csv_reader)   # for skip header
    for i in csv_reader: # read row
        print(i) 

# using dictReader    give a dictionry
from csv import DictReader
with open ('file.csv','r') as rf:
    csv_dic = DictReader(rf)   #delimiter=( | )
    for i in csv_dic:
        print (i) 
        print (i['name'])     # use as dict   in " " 
