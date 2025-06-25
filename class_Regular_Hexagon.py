import math
import Static_method
import class_shape


class Regular_Hexagon(class_shape.Shape):
    def __init__(self , side):
        self.side =Static_method.method.chek_ang_get_digit( side)
    def get_area(self):
        return ((math.sqrt(3) *  3) / 2 )* (self.side**2)