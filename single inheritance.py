# class Person:
#     def __init__(self):
#         self.name =input("enter name:")
#         self.age = int(input("enter age:"))
#
#     def show(self):
#             print("Name:",self.name,"Age:",self.age)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter roll no:"))
#         self.mark=int(input("enter mark:"))
#
#     def show(self):
#         super().show()
#         print("Roll no:",self.rollno,"mark:",self.mark)
#
#     def updatemark(self):
#         self.mark=int(input("enter update mark:"))
#
#
# s=Student()
# s.show()
# s.updatemark()


# class Category():
#     def __init__(self):
#         self.category_name=input("Enter the category name:")
#     def showcategory(self):
#         print("category name:",self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input("Enter the product name:")
#         self.price=float(input("Enter the product price:"))
#         self.quantity=int(input("Enter the product quantity:"))
#
#     def total_price(self):
#         total_price=self.price * self.quantity
#         print("total price:",total_price)
#
# p=Product()
# p.showcategory()
# p.total_price()





class Company():
    def __init__(self):
        self.company_name=input("Enter the company name:")
        self.location=input("Enter the location:")
    def display_company(self):
        print("Company Name:",self.company_name)
        print("Location:",self.location)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("Enter the employee ID:"))
        self.empname=input("Enter the employee name:")
        self.salary=int(input("Enter the salary:"))

    def display_details(self):
        super().display_company()
        print("Employee ID:",self.empid)
        print("Employee Name:",self.empname)
        print("Salary:",self.salary)

    def update_salary(self):
        self.salary=self.salary +(self.salary *10/100)
        print("Salary after 10% increment:",self.salary)

e=Employee()
e.display_details
e.update_salary()