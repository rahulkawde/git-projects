# Area of cicle and parimeter
class circle():                         #make circle class
    def __init__ (self,r):              # take self as radius
        self.radius = r                 # radius as r

    def area(self):                     #function of area
        return self.radius**2*3.14      # pie r(square)

    def parimeter(self) :               # function for parimeter
        return 2*self.radius*3.14       # 2 pie r

new_circle = circle(4)
print ('area: ',new_circle.area())
print ('parimeter:',new_circle.parimeter())   

       