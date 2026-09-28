#write a program to create a list 5 random 3 digit numbers
import random

l = []

for i in range(5):
    n = random.randint(100, 1000)
    l.append(n)

print(l)
# write a program to create a 5 digit random otp number

import random
otp=random.randint(10000,99999)
print(otp)



#write a program to find the position of a character in a string
s = input("Enter string: ")
ch = input("Enter character: ")

p = s.find(ch)

print("Position:", p)

#define a function that takes a string as argument and returns a new dictionary
def char_count(s):
    d = {}

    for ch in s:
        d[ch] = s.count(ch)

    return d

s = input("Enter string: ")
print(char_count(s))
#where keys are character and values are count of eachcharcter
def char_count(s):
    d = {}

    for ch in s:
        d[ch] = s.count(ch)

    return d

s = input("Enter string: ")
print(char_count(s))
#Define a function that takes string as argument and print the count of
# digits,spaces,letters in that string
def count_characters(s):
    digits = 0
    spaces = 0
    letters = 0

    for ch in s:
        if ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        elif ch.isalpha():
            letters += 1

    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Letters:", letters)

text = input("Enter a string: ")
count_characters(text)