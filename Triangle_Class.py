import class_Rectangle
import Static_method

class Triangle(class_Rectangle.Rectangle):
    def __init__(self  ,high , side ):
        super().__init__(high , side)
    def get_Perimeter(self):
        self.other_side = Static_method.method.chek_ang_get_digit(input("nust 2  enter other side"))
        self.other_side2 = Static_method.method.chek_ang_get_digit(input("enter anither one"))
        return self.side+self.other_side2+self.other_side

    def get_area(self):
        return (super().get_area())/2