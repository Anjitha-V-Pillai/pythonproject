#sum of 2 numbers
a=lambda a,b:a+b
print(a(2,3))

a=lambda a,b,c:a*b*c
print(a(2,3,4))

a=lambda x:x**3
print(a(2))

a=lambda x:x[0]
print(a('Ammu'))

a=lambda x:len(x)
print(a("Sara"))

a=lambda x:x[::-1]
print(a("Sara"))

d = {'name': 'Anu', 'age': 23}
name=lambda d:d['name']
print(name(d))

l=[10,20,30,40]
a=lambda l:l[1]
print(a(l))

a=lambda x:x+10
print(a(20))

# list map
l=[1,2,3,4]
print(list(map(lambda x: x**2,l)))
print(tuple(map(lambda x: x**2,l)))
print(set(map(lambda x: x**2,l)))




#create a new list of cubes
l=[1,2,3,4]
print(list(map(lambda x: x**3,l)))
#create a new list of square roots
l=[25,36,81,100]
print(list(map(lambda x: x**0.5,l)))

#create a new list of lengths

colors=['red','green','blue','yellow','black']
#create a new list of first characters
print(list(map(lambda x:len(x),colors)))
#create a new list of last characters
print(list(map(lambda x:x[0], colors)))
#create a new list of reverse of each elemnt
print(list(map(lambda x:x[-1],colors)))
#Given a list l=[23,78,12,56]
#Add 10 to each element in the given sequence
l=[23,78,12,56]
print(list(map(lambda x:x+10,l)))
##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
  {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# # create a new list of emails
print(list(map(lambda x:x['email'],l)))