class Person:
    count = 0           # class variable
    def __init__(self,name,last,age):  # init call
        Person.count += 1           # add 1 in count
        self.name = name
        self.last_name = last
        self.age = age
        

p1 = Person("rahul","kawde",23)
p2 = Person("sachin","kawde",21)

print(Person.count)
