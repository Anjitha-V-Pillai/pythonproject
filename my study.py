# 3, 6, 9, 12, 15, 18
for i in range(3,19,3):
    print(i,end=" ")
print()
# Print:
# 5, 10, 15, 20, 25, 30
for i in range(5,31,5):
    print(i,end=" ")
print()
# Print:
# 10, 20, 30, 40, 50
for i in range(10,51,10):
    print(i,end=" ")
print()
# Print:
# 9, 18, 27, 36, 45
for i in range(9,46,9):
    print(i,end=" ")
print()
# Print:
# 100, 90, 80, 70, 60
for i in range(100,59,-10):
    print(i,end=" ")
print()

# 11, 13, 15, 17, 19
# Print:
for i in range(11,20,2):
    print(i,end=" ")
print()
# 12, 14, 16, 18, 20
# Print:
for i in range(12,21,2):
    print(i,end=" ")
print()
# 21, 23, 25, 27, 29
# Print:
for i in range(21,30,2):
    print(i,end=" ")
print()
# 30, 28, 26, 24, 22
# Print:
for i in range(30,21,-2):
    print(i,end=" ")
print()
# 50, 45, 40, 35, 30
for i in range(50,29,-5):
    print(i,end=" ")
print()

# Level 3: Squares and Cubes
# Print the squares:
# 36, 49, 64, 81, 100
for i in range(6,11):
    print(i **2,end=" ")
print()
# Print the cubes:
# 1, 8, 27, 64, 125
for i in range(1,6):
    print(i**3,end=" ")
print()
# Print:
# 16, 25, 36, 49, 64
for i in range(4,9):
    print(i**2,end=" ")
print()

# Print multiples of 8 up to 80.
for i in range(8,81,8):
    print(i,end=" ")
print()
# Print multiples of 9 up to 90.
for i in range(9,91,9):
    print(i,end=" ")
print()
# Print multiples of 11 up to 110.
for i in range(11,111,11):
    print(i,end=" ")
print()
# Print multiples of 12 up to 120.
for i in range(12,121,12):
    print(i,end=" ")
print()


# Find the sum of:
# 2, 4, 6, 8, 10
sum=0
for i in range(2,11,2):
    sum=sum+i
print(sum,end=" ")
print()
# Find the sum of:
# 5, 10, 15, 20, 25
sum=0
for i in range(5,26,5):
    sum=sum+i
print(sum,end=" ")
print()
# Find the sum of all numbers from 1 to 50.
sum=0
for i in range(1,51):
    sum=sum+i
print(sum,end=" ")
print()

# Find the sum of all even numbers from 1 to 100.
sum=0
for i in range(2,101,2):
    sum=sum+i
print(sum,end=" ")
print()
# Find the sum of all odd numbers from 1 to 100.
sum=0
for i in range(1,100,2):
    sum=sum+i
print(sum,end=" ")
print()


# Find the product of:
# 1, 2, 3, 4, 5
product=1
for i in range(1,6):
    product=product*i
print(product,end=" ")
print()
# Find the product of all even numbers from 2 to 10.
product=1
for i in range(2,11,2):
    product=product*i
print(product,end=" ")
print()
# Find the product of all numbers divisible by 5 between 1 and 50.
product=1
for i in range(1,51):
    if i%5==0:
        product=product*i
print(product,end=" ")
print()
# Find the product of all numbers divisible by 3 between 1 and 30.
product=1
for i in range(1,31):
    if i%3==0:
        product=product*i
print(product,end=" ")
print()

# Count the even numbers between 1 and 100.
count=0
for i in range(1,101):
    if i%2==0:
     count=count+1
print(count,end=" ")
print()
# Count the odd numbers between 1 and 100.
count=0
for i in range(1,101):
    if i%2!=0:
        count=count+1
print(count,end=" ")
print()
# Count the numbers divisible by 7 between 1 and 100.
count=0
for i in range(1,101):
    if i%7==0:
        count=count+1
print(count,end=" ")
print()
# Count the numbers divisible by 5 and 3 between 1 and 100.
count=0
for i in range(1,101):
    if i%5==0 and i%3==0:
        count=count+1
print(count,end=" ")
print()
# Count the three-digit numbers divisible by 9.
count=0
for i in range(100,1000):
    if i%9==0:
        count=count+1
print(count,end=" ")
print()