#write a program to find BMI(Body Mass Index)
weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight / (height ** 2)
print("BMI =", bmi)
if bmi <= 18.4:
    print("Underweight")
else:
    if bmi >= 18.5 and bmi <= 24.9:
        print("Normal")
    else:
        if bmi >= 25.0 and bmi <= 39.9:
            print("Overweight")
        else:
            print("Obese")

#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

#2.# A toy vendor supplies three types of toys:



# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

code = int(input("Enter product code: "))
amount = float(input("Enter order amount: "))

if code == 1:
    if amount > 1000:
        amount = amount - amount * 10 / 100
    print("Net Amount =", amount)

else:
    if code == 2:
        if amount > 100:
            amount = amount - amount * 5 / 100
        print("Net Amount =", amount)

    else:
        if code == 3:
            if amount > 500:
                amount = amount - amount * 10 / 100
            print("Net Amount =", amount)
        else:
            print("Invalid Product Code")

#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number
n=int(input("enter the number: "))
if n%3==0:
    if n%5==0:
        print("fizzbuzz")
    else:
        print('fizz')
else:
    if n%5==0:
        print("buzz")
    else:
        print(n)
