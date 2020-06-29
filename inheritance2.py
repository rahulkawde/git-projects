# multilevel inheritance
# Method resolution order:
# isinstance()  issubclass()
# overwrite instance mehod


class Phone:    # parent class/base class
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = max(price,0)

    def make_call(self,number):                        #instance method
        return f"calling {number}..."

    def full_name(self):
        return f"mobile name is {self.name}{self.model} "

    def __len__(self):       #dunder
        return len(self.full_name())    
# inheritane with 2 ways
class Smartphone(Phone):    #derived class/child class
    def __init__(self,name,model,price,ram,rom,camera):
        # Phone.__init__(self,name,model,price)      # base class__init__   1st way
        super().__init__(name,model,price)            # handling variable    2nd way
        self.ram=ram
        self.rom=rom
        self.camera=camera
# multilevel inheritance        
class FlagshipPhone(Smartphone):  
    def __init__(self,name,model,price,ram,rom,camera,front_camera):
        super().__init__(name,model,price,ram,rom,camera)
        self.front_camera= front_camera 
# overwrite instance mehod
    def full_name(self):
        return f"mobile name is {self.name}{self.model} and front camera of{self.front_camera} "  




phone= Phone('nokia','1100',1000)  
smartphone= Smartphone('appple', '6s',24000, '2gb','32gb', '12mp') 
flagshipphone= FlagshipPhone('oneplus','5t',30000,'3gb','64gb','24mp','16mp')  

print(phone.full_name())
print(smartphone.full_name() + f'and price is{smartphone.price}')
print(flagshipphone.full_name() + f'and price is {smartphone.price} ') # overwrite
# isinstance()  issubclass()
print(isinstance(smartphone,Phone))    #(obj,class)
print(isinstance(flagshipphone,Phone))
print(issubclass(FlagshipPhone,Smartphone))  #(class,subclass)
#method revolution order
# print(help(FlagshipPhone)) 
#    #(help(class))
# Method resolution order:
#  |      FlagshipPhone
#  |      Smartphone
#  |      Phone
#  |      builtins.object

#dunder   __str__,__repr__
print(len(phone))

