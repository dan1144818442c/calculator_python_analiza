import math
import Static_method
import class_shape

class Circle(class_shape.Shape):
    def __init__(self , radius):
        self.radiud = Static_method.method.chek_ang_get_digit( radius)

    def get_area(self):
        return math.pi*(self.radiud**2)
    