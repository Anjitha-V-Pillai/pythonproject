# # i=1
# # while(i<=5):
# #     print(i)
# #     i=i+1
# # print("hello")
#
# #while
#
#
# # # #1,2,3,4,5,.....100
# i=1
# while(i<=100):
#     print(i,end=" ")
#     i=i+1
# print()
# # # #1,3,5,7,9,11,13,15
#
# i=1
# while (i<=15):
#     print(i)
#     i=i+2
#
# # #2,4,6,8,10,12
#
# i=2
# while(i<=12):
#     print(i)
#     i=i+2
#
# #1,4,9,16,25
#
# i=1
# while(i<=5):
#     print(i**2)
#     i=i+1
# # #1,4,7,10,13,16,
#
# i=1
# while(i<=16):
#     print(i)
#     i=i+3
# #10,20,30,40,50,60,70,80
#
# i=10
# while i<=80:
#     print(i)
#     i=i+10
#
# #3,6,9,12,15,18,21
# i=3
# while (i<=21):
#     print(i)
#     i=i+3
#
# #5,4,3,2,1
# i = 5
# while i >= 1:
#     print(i)
#     i = i-1
#
# #8,6,4,2,0
# i=8
# while(i>=0):
#     print(i)
#     i=i-2
#
# #100,101,102,.....200
# i=100
# while(i<=200):
#     print(i)
#     i=i+1
#
#
# #print all 4 digit numbers(1000-9999)
# i=1000
# while(i<=9999):
#     print(i)
#     i=i+1

#print those numbers that are divisible by 3 in the range(1,50)
# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i,end=" ")
#     i=i+1
# print()

# #print those 3 digits numbers that are divisible by 5 and 7
# i=100
# while(i<=999):
#     if(i%5==0 and i%7==0):
#         print(i,end=" ")
#     i=i+1
# print()
#
#
# #print those numbers in the rang (100,200) which contain digit "3
#
# i=100
# while(i<=200):
#     s=str(i)
#     if("3" in s):
#         print(i,end=" ")
#     i=i+1
# print()
#
# #print those numbers that are divisible by 3 in the range(1,50)
# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i,end=" ")
#     i=i+1
# print()
#
# #count of those nuthat are divisible by 3 in the range(1,50)
# i=1
# count=0
# while(i<=50):
#     if(i%3==0):
#         print(i,end=" ")
#         count=count+1
#     i=i+1
# print(count)
#
#
# #print those numbers in the rang (100,200) which contain digit "3
#
# i=100
# count=0
# while(i<=200):
#     s=str(i)
#     if("3" in s):
#         print(i,end=" ")
#         count=count+1
#     i=i+1
# print("count is:",count)
#
# #1,2,3,4,5-sum of series
#
# i=1
# sum=0
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print(sum)
#
# # product of series
# i=1
# product=1
# while(i<=5):
#     product=product*i
#     i=i+1
# print(product)
#
# #sum of first 10 even numbers
# i=1
# sum=0
# while(i<=20):
#     sum=sum+i
#     i=i+2
# print(sum)
#
# #product of first 10 even numbers
# i=1
# product=1
# while(i<=20):
# #     product=product*i
# #     i=i+2
# # print(product)
#
#
# #4,9,14,19,24,29
# i=4
# while(i<=39):
#     print(i,end=" ")
#     i=i+5
#
# #sum of series 1,3,5,7,9,11
# i=1
# sum=0
# while(i<=11):
#    sum=sum+i
#    i=i+2
# print(sum)
#
# #product numbers divisible by 3 and 5 upto range(1,50)
# i=1
# product=1
# while(i<=50):
#     if i%3==0 and i%5==0:
#         product=product*i
#     i=i+1
# print(product)
#
# #count of 3 digit divisible by 7
# i=100
# count=0
# while(i<=999):
#     if i%7==0:
#         count=count+1
#     i=i+1
# print(count)


#factorial of a number
# i=1
# n=int(input("enter the number: "))
# fact=1
# while(i<=n):
#     fact=fact*i
#     i=i+1
# print("factorial=",fact)
#
#
# #multiplication table of a number
# n=int(input("enter the number: "))
# i=1
# while(i<=n):
#     print(n,"*",i ,"=", n*i)
#     i=i+1

# #2, 6, 10, 14, 18, 22, 26, 30
# i=2
# while(i<=30):
#     print(i)
#     i=i+4
#
# #50, 45, 40, 35, 30, 25, 20, 15
# i=50
# while(i>=15):
#     print(i,end=" ")
#     i=i-5

# Find the sum of the series:
#
# 5, 10, 15, 20, 25
i=5
sum=0
while i<=25:
    sum=sum+i
    i=i+5
print(sum)