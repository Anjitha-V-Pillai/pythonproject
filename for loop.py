# # # # # # #string
# # # # # #
# # # # # # s="hello"
# # # # # # for i in s:
# # # # # #     print(i)
# # # # # #
# # # # # # #list
# # # # # #
# # # # # # l=["red",'blue','green']
# # # # # # for i in l:
# # # # # #     print(i)
# # # # # #
# # # # # # #set
# # # # # # s={1,2,3,4,5}
# # # # # # for i in s:
# # # # # #     print(i)
# # # # # #
# # # # # # #dictionary
# # # # # # d={"a" :10,"b" :20,"c" :30}
# # # # # # for i in d:
# # # # # #     print(i)
# # # # # #
# # # # # #
# # # # # # #dictionary
# # # # # # d={"a" :10,"b" :20,"c" :30}
# # # # # # for i in d.values():
# # # # # #     print(i)
# # # # #
# # # # # #given list
# # # # # # l=[12,34,56,45,89,16,69,33]
# # # # # # print each number in a list
# # # # # l=[12,34,56,45,89,16,69,33]
# # # # # for i in l:
# # # # #     print(i)
# # # # # # print even numbers
# # # # # l=[12,34,56,45,89,16,69,33]
# # # # # for i in l:
# # # # #     if i%2==0:
# # # # #         print(i)
# # # # #
# # # # # # print those numbers that are divisible by 5
# # # # # l=[12,34,56,45,89,16,69,33]
# # # # # for i in l:
# # # # #     if i%5==0:
# # # # #         print(i)
# # # # # # print those numbers that contain digit 3
# # # # # l=[12,34,56,45,89,16,69,33]
# # # # # for i in l:
# # # # #     if ("3" in str(i)):
# # # # #         print(i,end=" ")
# # # #
# # # #
# # # # # # give  a string
# # # # # s="hello world"
# # # # # for i in s:
# # # # #     print(i,end="")
# # # # # print()
# # # # # s="hello world"
# # # # # for i in s:
# # # # #     if i not in "aeiouAEIOU":
# # # # #         print(i,end=" ")
# # # # # d = {'n1':25, 'n2':46, 'n3':89, 'n4':24}
# # # # # print each value
# # # # # print odd values
# # # # # d = {'n1':25, 'n2':46, 'n3':89, 'n4':24}
# # # # # for i in d.values():
# # # # #     print(i)
# # # # #
# # # # # d = {'n1':25, 'n2':46, 'n3':89, 'n4':24}
# # # # # for i in d.values():
# # # # #     if i%2!=0:
# # # # #         print(i)
# # # #
# # # # # Given a list l=["red",'green','orange','blue','black','yellow']
# # # # # print each color
# # # # # l = ["red", 'green', 'orange', 'blue', 'black', 'yellow']
# # # # # # for i in l:
# # # # # #     print(i)
# # # # # # print color starting with 'b'
# # # # l = ["red", "green", "orange", "blue", "black", "yellow"]
# # # # for i in l:
# # # #     if (i[0]=="b"):
# # # #         print(i)
# # # # # # print color whose length is greater than 5
# # # # l = ["red", "green", "orange", "blue", "black", "yellow"]
# # # # for i in l:
# # # #     if len(i)>5:
# # # #         print(i)
# # # # # Given a list l=[10,'arun','amal',35,3.6,6.9,89]
# # # #
# # # # # print  string values
# # # # l=[10,'arun','amal',35,3.6,6.9,89]
# # # # for i in l:
# # # #     if type(i)==str:
# # # #         print(i)
# # # # # print float values
# # # # l=[10,'arun','amal',35,3.6,6.9,89]
# # # # for i in l:
# # # #     if type(i)==float:
# # # #         print(i)
# # #
# # # # l=[45,78,90,12,67]
# # # #sum of list
# # # l=[45,78,90,12,67]
# # # sum=0
# # # for i in l:
# # #     sum=sum+i
# # # print("sum is =",sum)
# # # # product of even numbers
# # # l=[45,78,90,12,67]
# # # product=1
# # # for i in l:
# # #     if i%2==0:
# # #         product=product*i
# # # print("product is =",product)
# # # # count of odd values
# # # l=[45,78,90,12,67]
# # # count=0
# # # for i in l:
# # #     if i%2!=0:
# # #         count=count+1
# # #
# # # print("count=",count)
# #
# #
# # # # 1,2,3,4,5
# # # for i in range(1,6):
# # #     print(i,end=" ")
# # # print()
# # # # 1,3,5,7,9
# # # for i in range(1,10):
# # #     print(i,end=" ")
# # # print()
# # # # 2,4,6,8,10
# # # for i in range(2,11,2):
# # #     print(i,end=" ")
# # # print()
# # # # # 1,4,9,16,25
# # # for i in range(1,6):
# # #     print(i**2,end=" ")
# # # print()
# # # # 4,9,14,19,24,29,34,39
# # # for i in range(4,40,5):
# # #     print(i,end=" ")
# # # print()
# # # #5,4,3,2,1
# # # for i in range(5,0,-1):
# # #     print(i,end=" ")
# # # print()
# # # # 8,6,4,2,0
# # # for i in range(8,-1,-2):
# # #     print(i,end=" ")
# # # print()
# # # # 7,14,21,28,35,42
# # # for i in range(7,43,7):
# # #     print(i,end=" ")
# # # print()
# #
# # #100,200,.....1000
# # for i in range(100,1001,100):
# #     print(i,end=" ")
# # print()
# # # 1,8,27,64,125
# # for i in range(1,6):
# #     print(i**3,end=" ")
# # print()
# # # find 3 digit divisible by 3
# # for i in range(100,1000):
# #     if i%3==0:
# #         print(i,end=" ")
# # print()
# # # print reverse of each colour
# # colors=["red","green","blue",'yellow',"black"]
# # for i in colors:
# #     print(i[::-1])
#
# # # print each digit in a number
# # n=1234
# # for i in str(n):
# #     print(i,end=" ")
# # print()
# # # sum of digit of number
# # sum=0
# # n=1234
# # for i in str(n):
# #     sum=sum+int(i)
# # print(sum)
# # print()
#
# # given a list
# l=[1,2,3,4]
# # print sqaures of each number
# for i in l:
#     print(i**2,end=" ")
# print()
# # create new list with each num
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)
# print()
#
# # set
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)
# print()

# # give a string
# s="hello world"
# # create a new string with only vowels
# new=""
# vowels="aeiouAEIOU"
# for i in s:
#     if i in vowels:
#         new=new+i
# print(new)
# print()
# create a new dict where key are numbers and values are square of each number
# new{1:1,2:4....4:16}
# l=[1,2,3,4]
# new={}
# for i in l:
#     new[i]=i**2
# print(new)
# reverse of a string
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# print()

# # reverse of a number
# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)
# print()
