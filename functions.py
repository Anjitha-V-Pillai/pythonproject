# #
# #
# # # sum of 2 numbers
# # def add():
# #     "addition of two numbers"
# #     n1=int(input("enter first number:"))
# #     n2=int(input("enter second number:"))
# #     s=n1+n2
# #     print("sum",s)
# #     return
# # add()
# #
# # # define a function display"hello your name"
# # def display_name():
# #     n=input("enter your name:")
# #     print("hello",n)
# #     return
# # display_name()
# #
# # # define a function find factorial of a number
# # def fact():
# #     n=int(input("enter number:"))
# #     f=1
# #     for i in range(1,n+1):
# #         f=f*i
# #         print("factor",i)
# #         return
# # fact()
# # # define a fun to find the count of a specific character in a given string
# # def count():
# #     n=input("enter the character:")
# #     count=0
# #     s=input("enter string:")
# #     for i in s:
# #         if(i==count):
# #             count+=1
# #         print("count",count)
# #         return
# # count()
# #
# # # define fun to check whether a numbr is prime or not
# # def prime():
# #     n=int(input("enter number:"))
# #     if(n>1):
# #         for i in range(2,n):
# #             if(n%i==0):
# #                 print("not prime")
# #                 break
# #         else:
# #             print("prime")
# #     else:
# #         print("number is neither prime nor composite")
# #     return
# # prime()
# #
# # # define a function to find factors of a number
# # def fact():
# #     n=int(input("enter number:"))
# #     for i in range(1,n+1):
# #         if(n%i==0):
# #             print(i)
# #     return
# # fact()
#
# # sum of 2 numbers
# def add(n1,n2):
#     # n1=int(input("enter first number:"))
#     # n2=int(input("enter second number:"))
#     s=n1+n2
#     print("sum is:",s)
# add(23,20)
#
# # define a function that amount,rate,arguments
# # amd find the simple interest value
# # def simple_interest(amount,years,rate):
# #     si=amount*years*rate/100
# # amount=float(input("enter amount:"))
# # years=float(input("enter years:"))
# # rate=float(input("enter rate:"))
# # print("simple interest",amount*years*rate/100)
# #
# # simple_interest(amount,years,rate)
#
# def add(n1,n2):
#     s=n1+n2
#     print("sum is:",s)
#     return s
# a=add(23,34)
# print("a=",a)
#
# s="hello"
# a=len(s)
# print("len=",a)
#
# l=[1,2,3]
# a=l.append(5)
# print(a)
#
# # define  a function  that takes 2 numbers  as arguments and sum of result
# # call the fun and print resul
# def add(n1,n2):
#     s=n1+n2
#
#     return s
# a=add(20,23)
# print("sum is:", a)


l=[10,20,30,40]
new={i:l[i] for i in range(0,len(l))}
print(new)
s="python coding  is easy and fun"
new={i:len(i) for i in s.split()}
print(new)