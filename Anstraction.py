from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        self

    @abstractmethod
    def get_perimeter(self):
        pass
class Rectangle()