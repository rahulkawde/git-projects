#property() and setter()

class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model= model
        self.price=max(price,0)      # max fro -ve price
    
    @property                       # property method
    def specification(self):
        return f'{self.name} {self.model} {self.price} is full specification.'
    # getter()-----> .setter()
    @property
    def price_1(self):
        return self.price              # getter()

    @price_1.setter
    def price_1(self,new_price):
        self.price=max(new_price,0)    #setter()
        
    def make_call(self,number):                        #instance method
        return f"calling {number}..."

    def full_name(self):
        return f"mobile name is {self.name}{self.model} "

p1= Phone('nokia','1100',1000)          #instance

print(Phone.full_name(p1))
p1.price= -500          #update price
# print(p1.price_1(-500))                  #when price is -ve =0
print (p1.specification)        #with help of property we update price







