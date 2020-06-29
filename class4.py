#class mehod as constructor

class Person:
    count_instance= 0       # class variable
    def __init__(self,a,b,c) :
        Person.count_instance+=1
        self.first=a
        self.last=b
        self.age=c   
    @classmethod     # classmethod as constructor
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first,last,age)  # class(variables)

    @classmethod            # create class method
    def count_instances(cls):
        return f"you have {cls.count_instance} instance of {cls.__name__} class" 

    @staticmethod                   # create static method
    def hello():
        print("this is static method")

    def full_name(self):            #  create instance method
        return f"{self.first} {self.last}"    

p1= Person('rahul','kawde',23) 
p2 = Person('sachin','kawde',21)

# object/instance

print (p1.first)
print (p1.__dict__)
print (Person.count_instances())   # use class method
print (Person.full_name(p1))     # use instance method
print (Person.full_name(p2))     # use constructor
print ( Person.from_string("rahul,kawde,23"))
Person.hello()