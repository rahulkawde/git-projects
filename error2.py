class Mobile:
    def __init__(self,name):
        self.name=name

class Mobilestore:
    def __init__(self):
        self.mobiles  = []

    def add_mob(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile object should be in Mobile class')  


nokia = Mobile('nokia 1100')
samsung = 'samsung g2'
mobostore = Mobilestore()
# mobostore.add_mob(samsung)      # error
mobostore.add_mob(nokia)
# print(mobostore.mobiles)    
new_mobo = mobostore.mobiles     # store in variable
print(new_mobo[0].name)        


