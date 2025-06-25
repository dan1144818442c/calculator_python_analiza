import class_shape


class Rectangle(class_shape.Shape):
    def __init__(self , high , side):
        self.high = high
        self.side = side

    def get_area(self):
        return  self.side*self.high

