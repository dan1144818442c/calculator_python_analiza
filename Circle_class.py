import math

import class_shape

class Circle(class_shape.Shape):
    def __init__(self , radius):
        self.radiud = radius
    def get_area(self):
        return math.pi*(self.radiud**2)
    