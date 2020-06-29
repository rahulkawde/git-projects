#class create
class Laptop:
    def __init__(self,a,b,c): # create class
        #instance variable  
        self.name = a
        self.model = b
        self.price = c
        self.laptop_name = a + " "+ b  # comb a+b
    def discout(self):    # create method in class(don't forget self)
        disc= (self.add_discout/100)*self.price
        return self.price - disc 

laptop1 = Laptop('acer','e-571',22000)
laptop2 = Laptop( 'DELL','d-55',25000)  
laptop2.add_discout= 10
laptop3 = Laptop('apple','macboook pro', 150000)
laptop3.add_discout= 40

print(laptop3.__dict__)
print(laptop3.discout())

print(laptop1.__dict__)
print(laptop1.name)

print(laptop2.__dict__)
print(laptop2.price)
print(laptop2.laptop_name)
print(laptop2.discout())
