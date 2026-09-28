# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

class Movie():
    def __init__(self):
        self.moviename=input("Enter the movie name:")
        self.year=input("Enter the year:")
        self.language=input("Enter the language:")
        self.director=input("Enter the director:")
        self.rating=float(input("Enter the rating:"))
    def display_details(self):
        print("movie name:",self.moviename)
        print("year:",self.year)
        print("language:",self.language)
        print("director:",self.director)
        print("rating:",self.rating)
    def update_rating(self):
        self.rating=float(input("Enter the update rating of the movie:"))

m=Movie()
m.display_details()
m.update_rating()
m.display_details()


# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.
#

class Vehicle():
    def __init__(self):
        self.brand = input("Enter the brand of the vehicle: ")
        self.model=input("Enter the model of the vehicle:")
        self.color=input("Enter the color of the vehicle:")
        self.year=int(input("Enter the year of the vehicle:"))
    def display_vehicle(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("color:",self.color)
        print("year:",self.year)

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.mileage=float(input("Enter the mileage of the car:"))
    def dispaly_car(self):
        super().display_vehicle()
        print("mileage:",self.mileage)

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.cc=float(input("Enter the car cc of the bike:"))

    def display_bike(self):
        super().display_vehicle()
        print("cc:",self.cc)
print("car details:")

c=Car()
c.dispaly_car

print("bike details:")
b=Bike()
b.display_bike()