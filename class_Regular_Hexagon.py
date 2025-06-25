import math

import class_shape


class Regular_Hexagon(class_shape.Shape):
    def __init__(self , side):
        self.side = side
    def get_area(self):
        return ((math.sqrt(3) *  3) / 2 )* (self.side**2)