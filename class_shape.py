class Shape:
    def get_area(self):
        pass
    def get_Perimeter(self):
        pass
    def __add__(self, other):
        if not isinstance(other, Shape):
            print("must enter just object of type Shape")
            return 0
        return (self.get_area()) + ( other.get_area())

    def __gt__(self, other):
        if not isinstance(other, Shape):
            print("must enter just object of type Shape")
            return 0
        return (self.get_area() > other.get_area())

    def __sub__(self, other):
        if not isinstance(other,Shape):
            print("must enter just object of type Shape")
            return 0
        return (self.get_area() - other.get_area())
    def __str__(self):
        "adfegtrhyj"
        return f"{self.__class__.__name__ } area : {self.get_area()}  Perimeter : {self.get_Perimeter()}"
    def __eq__(self, other):
        if not isinstance(other,Shape):
            print("must enter just object of type Shape")
            return 0
        return (self.get_area() == other.get_area()) and (self.get_Perimeter() == other.get_Perimeter())