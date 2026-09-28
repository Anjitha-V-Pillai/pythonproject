class Parent:
    def m1(self):
        print("in parent class method m1")
    def m2(self):
        print("in parent class method m2")

class child(Parent):
    def m3(self):
        print("in child class method m3")

    #method overriding
    #output:
    # in child class method m1
    # in parent class method m2
    # in child class method m3
    def m1(self):
        print("in child class method m1")

     # To print child and parent
    def m1(self):
        super().m1()

c=child()
c.m1()
c.m2()
c.m3()