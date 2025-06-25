import class_shape
import Static_method

class Rectangle(class_shape.Shape):
    def __init__(self , high , side):
        self.high = Static_method.method.chek_ang_get_digit(high)
        self.side = Static_method.method.chek_ang_get_digit(side)

    def get_area(self):
        return  self.side*self.high

    def get_Perimeter(self):
        return (self.side+self.high)*2


