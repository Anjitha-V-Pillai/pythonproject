# #global
#
# x=20
# print("outside function",x)
# def f():
#     print("inside function")
# f()

#local
def f():
    x=20
    print("inside function",x)
f()
print("outside function",x)

def g():
    y=30
    print("inside function",y)

f()
g()