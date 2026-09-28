# l = [1, 2, 1, 2, 3, 4, 4, 5, 6]
# d = {}
# for i in l:
#     d[i] = l.count(i)
# print(d)
#
#
# l = [11, 34, 78, 23, 90, 65]
#
# largest = max(l)
# l.remove(largest)
#
# second_largest = max(l)
#
# smallest = min(l)
# l.remove(smallest)
#
# second_smallest = min(l)
#
# print("Largest =", largest)
# print("Second largest =", second_largest)
# print("Smallest =", smallest)
# print("Second smallest =", second_smallest)
#
# # Largest number
# # Second largest number
# # Smallest number
# # Second smallest number
# l = [11, 34, 78, 23, 90, 65]
#
# l.sort()
#
# print("Smallest:", l[0])
# print("Second smallest:", l[1])
# print("Second largest:", l[-2])
# print("Largest:", l[-1])
#
# # The maximum salary
# # The minimum age
# l = [['arun', 23, 300000],
#      ['amal', 25, 500000],
#      ['anu', 27, 400000]]
#
# salary = [i[2] for i in l]
# age = [i[1] for i in l]
#
# print("Maximum salary =", max(salary))
# print("Minimum age =", min(age))
#
#
# # without using built in function
# l=[23,45,67,12,90,78]
# max=l[0]
# for i in l:
#     if(i > max):
#         max=i
# print("maximum",max)
#
# min=l[0]
# for i in l:
#     if(i < min):
#         min=i
# print("minimum",min)
l=[1,1,2,3,3,4]
l=list(set(l))
print(l)

l = [1, 1, 2, 3, 3, 4]
new=[]
for i in l:
    if i not in new:
        new.append(i)
print(new)


l1 = [13, 27, 30, 42, 57]
l2 = [13, 57, 89, 33, 80]
common=[]
for i in l1:
    if i in l2:
        common.append(i)
print(common)
# with using set function
s1=set(l1)
s2=set(l2)
print(list(s1.intersection(s2)))