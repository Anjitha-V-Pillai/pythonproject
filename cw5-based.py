# 1.
#
# Print all numbers between 1 and 100 that are divisible by 4 or 6.
for i in range(1,101):
    if i%4==0 or i%6==0:
        print(i,end=" ")
print()
#
# 2.
#
# Print the sum of all numbers divisible by 7 between 1 and 100.
sum=0
for i in range(1,101):
    if i%7==0:
        sum=sum+i
print(sum)
print()
#
# 3.
#
# Given two numbers a and b, print only the even numbers between them.
#
# Example:
#
a = 10
b = 20
for i in range(10,21,2):
    print(i,end=" ")
print()

# 4.
#
# Given a list:
#Print only the numbers greater than 40.
l = [12, 45, 67, 22, 89, 30]
for i in l:
    if i>40:
        print(i,end=" ")
print()
#
# 5.
#
# Given a list:
#
# l = [12, 45, 67, 22, 89, 30]
#
# Count how many numbers are greater than 40.
l = [12, 45, 67, 22, 89, 30]
count=0
for i in l:
    if i>40:
        count=count+1
print(count)
print()
# Lists
# 6.
#
# Create a new list containing the cube of each number.
#
# Input:
#
l=[2,3,4]
new=[]
for i in l:
    new.append(i**3)
print(new)
# Output:
#
# [8,27,64]
# 7.
#
# Create a new list containing only the even numbers.
#
# Input:
#
# [2,5,8,9,12]
l=[2,5,8,9,12]
new=[]
for i in l:
    if i%2==0:
        new.append(i)
print(new)
#
# Output:
#
# [2,8,12]
# 8.
#
# Create a new list by adding 10 to every element.
#
# Input:
#
# [5,10,15]
l=[5,10,15]
new=[]
for i in l:
    new.append(i+10)
print(new)
#
# Output:
#
# [15,20,25]
# 9.
#
# Replace every odd number with 0.
#
# Input:
#
l=[2,5,8,9]
new=[]
for i in l:
    if i%2!=0:
        new.append(0)
    else:
        new.append(i)
print(new)
#
# Output:
#
# [2,0,8,0]
# 10.
#
# Find the largest number in a list without using max().
l=[12,65,78,96,54,99,11,3]
largest=l[0]
for i in l:
    if i>largest:
        largest=i
print(largest)
# using max function
l=[12,65,78,96,54,99,11,3]
max=max(l)
print(max)
# Strings
# 11.
#
# Count the number of vowels in a string.
#
# Input:
#
s="python programming"
count=0
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        count=count+1
print(count)
# 12.
#
# Count the number of spaces in a string.
#
# Input:
#
s="python is easy"
count=0
for i in s:
    if i==" ":
        count=count+1
print(count)
# 13.
#
# Create a new string containing only uppercase letters.
#
# Input:
#
s="PyThOn123"
new={}
for i in s:
    if i[A-Z] in new:
        new=new+i
print(new)
# Output:
#
# PTO
# 14.
#
# Reverse every word in a sentence.
#
# Input:
#
# "python is easy"
#
# Output:
#
# nohtyp si ysae
# 15.
#
# Count how many times the letter 'a' appears in a string.
#
# Break & Continue
# 16.
#
# Print numbers from 1 to 100.
#
# Skip numbers divisible by 4.
# Stop when the number becomes greater than 60.
# 17.
#
# Given a list:
#
# l = [10,15,22,35,48,60]
#
# Print numbers until 48 is found.
#
# 18.
#
# Given a list:
#
# l = [10,15,22,35,48,60]
#
# Skip all numbers divisible by 5.
#
# Dictionary
# 19.
# d = {
# 101:["Arun",23],
# 102:["Amal",25],
# 103:["Anu",21]
# }
#
# Print only the ages.
#
# 20.
# d = {
# 101:["Arun",23],
# 102:["Amal",25],
# 103:["Anu",21]
# }
#
# Print the names of students whose age is greater than 22.