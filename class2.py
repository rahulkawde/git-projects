#class veriable

class Circle:                     #class
    pi = 3.14                     #class variable
    def __init__(self,a):
        self.radius= a
    def circumference(self):        #class method
        return 2 * (Circle.pi) * self.radius    

c1 =Circle(4)
c2 =Circle(8)
print(c2.circumference())
print(c1.__dict__)    #give dict of c1