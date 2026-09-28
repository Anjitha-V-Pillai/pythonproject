#write a program for swapping two numbers

a=2
b=3

# print("before")
# print(a)
# print(b)
# #using third variable or temporary variable
# temp=a
# a=b
# b=temp
#
# print("after")
# print(a)
# print(b)

#without using third variable
#
# a=2
# b=3
# print("before")
# print(a)
# print(b)
# a,b=b,a
# print("after")
# print(a)
# print(b)

#another method without using third variable

a=2
b=3
print("before")
print(a)
print(b)
a = a + b
b = a - b
a = a - b
print("after")
print(a)
print(b)