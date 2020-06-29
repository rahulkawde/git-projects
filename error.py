class Animal:
    def __init__(self,name):
        self.name= name

    def sound(self):        # for diiff
        raise NotImplementedError('you have to define sound')

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return 'bhow bhow'   

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed  
    def sound(self):
        return'meow meow'        

dog= (Dog("puppy","pug"))
cat= (Cat('pussy','street'))
print(cat.name)             # call name
print(dog.name)
print(dog.sound())          # call sound
print(cat.sound())