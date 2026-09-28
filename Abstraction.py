from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        self

    @abstractmethod
    def get_perimeter(self):
        pass
class Rectangle(Shape):
    def __init(self):
        self.length=int(input("Enter the length of the rectangle: "))
        self.breadth=int(input("Enter the breadth of the rectangle: "))
    def get_area(self):
        print("Area",self.length*self.breadth)
    def get_perimeter(self):
        print("Perimeter",2*(self.length*self.breadth))

r=Rectangle()
r.get_area()
r.get_perimeter()

class Square(Shape):
    def __init(self):
        self.length=int(input("Enter the length : "))
    def get_area(self):