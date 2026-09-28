# def fun(n,a=23):
#     print("name",n)
#     print("age",a)
#
# fun("arun",25)
# fun("arun")

# arbitary positional arguments
def fun(*args):
    print(args)
fun(10,20)
fun(10,20,30)
fun(10,20,30,40)


# arbitary keyword arguments
def fun(**kwargs):
    print(kwargs)
fun(a=10,b=20)
fun(a=10,b=20,c=30)
fun(a=10,b=20,c=30,d=40)
fun(a=10,b=20,c=30,d=40,e=50)

# define a functon to find the sum of numbers using
# arbitary argument type
# def add(*args):
#     pass
# add(10,20)
# add(1,2,3,4)

def add(*args):
    s = 0

    for i in args:
        s = s + i

    print(s)
add(10, 20)
add(1, 2, 3, 4, 5)

# built in function
