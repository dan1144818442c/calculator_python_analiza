import class_Rectangle


class Triangle(class_Rectangle.Rectangle):
    def __init__(self  ,high , side ):
        super().__init__(high , side)
    def get_area(self):
        return (super().get_area())/2