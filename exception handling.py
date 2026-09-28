try:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    r=n1/n2

except:
    print("zero division error")

else:
    print("result",r)
finally:
    print("done")


# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

import math
while True:
    try:
        n=int(input("enter the  number:"))
        print("Factorial",math.factorial(n))
    except:
        print("invalid input")
    else:
        break

#Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
#and division based on user choice. Handle invalid inputs and division by zero using exception handling.
import math
try:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=int(input("enter your choice:"))
    if choice==1:
        print(n1+n2)
    elif choice ==2:
        print(n1-n2)
    elif choice==3:
        print(n1*n2)
    elif choice==4:
        print(n1/n2)
    else:
        print("invalid choice")
except ZeroDivisionError:
        print("Error: Cannot divide by zero")

# else:
#     print("Invalid choice")

except ValueError:
    print("Error: Please enter valid numbers")
# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
try:
    filename=input("enter the file name:")
    f=open(filename)
    content=f.read()

except FileNotFoundError:
    print("file not exist")
else:
    print(content)
    f.close()

#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

d = {"name": "arun", "age": 23, "place": "ekm"}

try:
    key = input("Enter a key: ")
    print("Value =", d[key])

except KeyError:
    print("Key does not exist")



