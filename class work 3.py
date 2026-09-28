# #Write a program to check whether two entered numbers are equal or not

n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
if n1==n2:
    print("the numbers are equal")
else:
    print("the numbers are not equal")


# #Write a program to check whether two entered words are equal or not
#
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if word1 == word2:
    print("Both words are equal")
else:
    print("Both words are not equal")


# #Write a program to find the maximum of two numbers

n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
if n1>n2:
    print("maximum number is:",n1)
else:
    print("maximum number is:",n2)


# #write a program to check whether the entered character is vowel or not

ch=input("enter your character: ")
vowel="aeiouAEIOU"
if ch in vowel:
    print("The entered character is a vowel")
else:
    print("The entered character is not a vowel")

# #Write a program to check whether the entered country name contains word 'land'

con=input("enter the country name: ")
if "land" in con:
    print("the country contain land")
else:
    print("the country contain no land")


# #write a program to check whether the entered number is 3 digit or not

n=int(input("Enter a number: "))
if n >= 100 and n <= 999:
    print("3-digit number")
else:
    print("Not a 3-digit number")


#write a program to check whether the entered string is  palindromde or not

s=input("enter the string: ")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Write a program to check whether a number is present in given list

l=[23,67,12,90]
n=int(input("enter the number:"))
if n in l:
    print("the number is present")
else:
    print("the number is not present")


#Write a program to check whether a key is prsent in a dictionary or not

d={101:'Arun',102:'Amal',103:'Anu'}
k=int(input("enter the number: "))
if k in d:
    print("key is present")
else:
    print("key is not present")


#Write a program to check whether the given password is strong/weak(if length lessthan 8 weak)

pas= input("enter the password:  ")
if len(pas)>8:
    print("The password is strong")
else:
    print("The password is weak")