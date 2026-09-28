
l=[1,2,3,4]
new=[5 for i in l]
print(new)


l=[1,2,3,4]
new=[i*2 for i in l]
print(new)


l=[1,2,3,4]
new=[i*3 for i in l]
print(new)

l=[23,56,34,12,89,90,24]
new=[i for i in l if i%2==0]
print(new)

l=[23,56,34,12,89,90,24]
new=[i for i in l if i>50]
print(new)


#create a new list of cubes
l=[1,2,3,4]
new=[i*3 for i in l]
print(new)
#create a new list of square roots
l=[25,36,81,100]
new=[i**0.5 for i in l]
print(new)


#create a new list of lengths
colors=['red','green','blue','yellow','black']
#create a new list of first characters
#create a new list of last characters
#create a new list of reverse of each elemnt

#Given a list
l=[23,78,12,56]
#Add 10 to each element in the given sequence
new=[i+10 for i in l]
print(new)
##given a list of dictionaries
l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
new=[i['email'] for i in l]
print(new)
# # create a new list of emails

# # #create a new list with square root of each element
l=[25,16,9,36]
new=[i**0.5 for i in l]
print(new)



# # #create a new list with square root of each element
# # l=[25,16,9,36]


# #Given a dictionary
d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
new=[i for i in d]
print(new)
# # create a list of marks
new=[i for i in d.values()]
print(new)

# #Given a list
l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
new=[i for i in l if type(i)==str]
print(new)
# #create a list of floats
new=[i for i in l if type(i)==float]
print(new)
# #create a list of positive numbers
new=[i for i in l if type(i)!=str and i>0]
print(new)

#
#
# #Given a list
fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
new=[i for i in fruits if len(i)>6]
print(new)
# #create a new list with elements whose value is divisible by 3 in range(1,101)
new=[i for i in range(1,101) if i%3==0]
print(new)
# Given
s="python coding  is easy and fun"
# # create a new list with only vowels
new=[i for i  in s if i in "AEIOUaeiou"]
print(new)

# set comprehension
s="python coding  is easy and fun"
# # create a new list with only vowels
new_set={i for i  in s if i in "AEIOUaeiou"}
print(new_set)

# dictionary comprenesion
l=[1,2,3,4]
new={}
for i in l:
    new[i]=i**2
    print(new)

l=[1,2,3,4]
new={i:i**2 for i in l}
print(new)

l=[10,20,30,40]
new={i:l[i] for i in range(0,len(l))}
print(new)

s="hello world"
for i in s:
    print(i)

s="hello world"
for i in s.split():
    print(i)

s="python coding  is easy and fun"
new={i:len(i) for i in s.split()}
print(new)