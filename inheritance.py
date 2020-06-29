class Phone:    # parent class/base class
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = max(price,0)

    def make_call(self,number):                        #instance method
        return f"calling {number}..."

    def full_name(self):
        return f"mobile name is {self.name}{self.model} "
# inheritane with 2 ways
class Smartphone(Phone):    #derived class/child class
    def __init__(self,name,model,price,ram,rom,camera):
        # Phone.__init__(self,name,model,price)      # base class__init__   1st way
        super().__init__(name,model,price)            # handling variable    2nd way
        self.ram=ram
        self.rom=rom
        self.camera=camera


phone= Phone('nokia','1100',1000)  
smartphone= Smartphone('appple', '6s',24000, '2gb','32gb', '12mp')        

print(phone.full_name())
print(smartphone.full_name() + f'and price is{smartphone.price}')