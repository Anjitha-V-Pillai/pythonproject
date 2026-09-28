# for i in range(1,6):
#     print(i)
# else:
#     print("hello")
# # use break condition
# for i in range(1,6):
#     if(i==3):
#         break
#     print(i)
# else:  #it works only after the normal execution of loop
#     print("hello")

# check whether a number is prime or not
num=int(input("Enter a number: "))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
    else:
        print("prime")
else:
    print("number is neither prime nor composite")