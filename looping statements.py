# # #using break
# # s="hello"
# # for i in s:
# #     if(i=="l"):
# #         break
# #     print(i)
# #
# # # continue
# #
# # s="hello"
# # for i in s:
# #     if(i=="l"):
# #         continue
# #     print(i)
# #
# # # pass
# # s="hello"
# # for i in s:
# #     if(i=="l"):
# #         pass
# #     print(i)
# #
# # s="hello"
# # for i in s:
# #     if(i=="e"):
# #         break
# #     print(i)
# #
# # s="hello"
# # for i in s:
# #     if(i=="h"):
# #         continue
# #     print(i)
#
# l=[25,67,34,78,17,44,82]
# # print all numbers
# for i in l:
#     print(i,end=" ")
# print()
#
# # stop the loop when i>50
# l=[25,67,34,78,17,44,82]
# for i in l:
#     if i>50:
#         break
#     print(i,end=" ")
# print()
# # skip all even numbers
# l=[25,67,34,78,17,44,82]
# for i in l:
#     if i%2==0:
#         continue
#     print(i,end=" ")
# print()
#
#
# # 2.
# # Given a list colors=['red','green','yellow','blue','orange','black']
# # #print all colors
# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     print(i,end=" ")
# print()
#
# # #print those colors starting with 'b' #blue black
# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     if i[0]=="b":
#
#         print(i,end=" ")
# print()
#
# # #print the first color starting with 'b' #blue
# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     if i[0]=="b":
#         print(i,end=" ")
#         break
# print()
# # #skips all colors starting with 'b'
# colors=['red','green','yellow','blue','orange','black']
# for i in colors:
#     if i[0]=="b":
#        continue
#     print(i,end=" ")
#
# print()
#
# # Given s="python coding is easy and fun"
# #
# # print all charcters upto a specific character(including that character)
# s="python coding is easy and fun"
# for i in s:
#     print(i, end="")
#     if i == "g":
#         break
#
# # write a prgm to check whether a number is Armstrong number
# num=int(input("enter the number:"))
# s=str(num)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if(sum==num):
#     print("Armstrong")
# else:
#     print("Not armstrong")

# factors of a number

# 6--1,2,3,6
# 8---1,2,4,8
# 5--1,5
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

# pass -looping statement
# working done but no operation
# for i in range(1,11):
#     pass
# print(i)

for i in range(1,11):
    if(i==3):
        pass
    else:
        print(i)

# output:1 2 4 5 6 7 8 9 10
# pass is anull statement
# act as a place holder
# for statement inside block

