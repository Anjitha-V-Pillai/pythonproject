# class A:
#     def f(self):
#         print("in class A function f")
# class B():
#     def f(self):
#         print("in class B fucntion f")
# class C():
#     def f(self):
#         print("in class C fucntion f")
# a=A()
# a.f()
# b=B()
# b.f()
#
#
# class Parent:
#     def f(self):
#         print("Parent function f")
# class Child(Parent):
#     def f(self):
#         print("Child function f")
# c=Child()
# c.f() #Child function f

# in same clss
class A:
    def f(self):
        print("in first function f")
    def f(self,a):
        print("in second fucntion f")
    def f(self,a,b):
        print("in third function f")


a = A()
# a.f()
# a.f(10)
#
a.f(10,30)