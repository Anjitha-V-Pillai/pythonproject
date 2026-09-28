# #write prgm to check the following
# # a number is divisible by 2 and 3
# # a number is divisible by 2 and not divisible by 3
# # a number is divisible by 3 and nnot divisible  by 2
# # a number is not divisible by  2 and 3
#
# n=int(input("enter the number: "))
# if n%2==0:
#     print("entered number is divisible by 2")
#     if n%3==0:
#         print("entered number is divisible by 3")
#     else:
#         print("entered number is not divisible by 3")
# else:
#     print("entered number is not divisible by 2")
#     if n%3==0:
#         print("entered number is divisible by 3")
#     else:
#         print("entered number is not divisible by 3")


        #chck whether the enterd number is positive even or odd
        # negative even or odd
n=int(input("enter the number: "))
if n>=0:
    print("positive number")
    if n%2==0:
        print("even")
    else:
        print("odd")
else:
    print("negative number")
    if n%2==0:
        print("even")
    else:
        print("odd")