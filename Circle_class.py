import math

import calculator


class Circle(calculator.Shape):
    def __init__(self , radius):
        self.radiud = radius
    def get_area(self):
        return math.pi*(self.radiud**2)
    