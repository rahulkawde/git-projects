# read write    o/p in final.csv
from csv import DictReader,DictWriter
with open ('file.csv','r') as rf:
    with open ('final.csv','w',newline='') as wf:
        csv_reader = DictReader(rf)
        csv_witer = DictWriter(wf,fieldnames=['name','email','age'])
        csv_witer.writeheader()
        for i in csv_reader:
            n,em,ag = i['name'],i['email'],i['age']
            csv_witer.writerow({
                'name': n,
                'email': em,
                'age': ag
            })

