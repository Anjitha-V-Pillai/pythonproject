# # # Q1.Define a function that takes 2 numbers and returns their product
def product(n1,n2):
   return n1*n2
result=product(10,2)
print("product is:",result)

# # Q2.Define a function that takes a string and returns number of vowels
def vowels(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count = count + 1
    return count

result = vowels("hello")
print(result)

# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
def area(length,breadth):
    return length*breadth
result=area(10,2)
print("area:",result)

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
def even_numbers(l):
    new=[]
    for i in l:
        if i %2==0:
            new.append(i)
    return new
l=[45,78,90,12,35]
result=even_numbers(l)
print("even numbers:",result)




# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]


l = [123, 345, 111, 678, 134, 809]

def fun(l):
    new = []

    for i in l:
        s = str(i)
        sum = 0
        for j in s:
            sum = sum + int(j)
        new.append(sum)
    return new

a = fun(l)
print(a)

#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# l=[12,34,78,12,67,34,90,23]
def unique_elements(l):
    new=[]
    for i in l:
        if i not in new:
            new=new+[i]
    return new
l=[12,34,78,12,67,34,90,23]
result=unique_elements(l)
print("unique elements:",result)


#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
def common_elements(l1,l2):
    new=[]
    for i in l:
        if i in l1 and i in l2:
            new.append(i)
    return new
l1=[12,34,56,78,90]
l2=[90,34,11,57,45]
result=common_elements(l1,l2)
print("common elements:",result)