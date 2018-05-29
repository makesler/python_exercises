class Circle:
  def area(self):
    return self.pi * self.radius ** 2
  def perimeter(self):
    return (self.pi * self.radius)*2
  def __init__(self, pi, radius):
    self.pi = pi
    self.radius = radius
    
#create an instance of Circle
x = Circle(3.14, 12)

print("AREA: ", x.area())         #prints area
print("PERIMETER: ", x.perimeter())    #prints perimeter
