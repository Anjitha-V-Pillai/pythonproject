s="python coding  is easy and fun"
def fun(s):
    new={}
    for i in s.split():
        new[i]=len(i)
    return new
a=fun(s)
print(a)

# define a function that takes a number as argument and check whether that number is spy number or not
# sum of digits=product of digit(spy number)

def spy(n):
    s=0
    p=1
    for i in str(n):
        s=s+int(i)
        p=p*int(i)
    if s==p:
        print("spy number")
    else:
        print(" not spy number")
n=int(input("enter number:"))
(spy(n))
