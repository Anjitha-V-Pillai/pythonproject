#
#
#
# l=[10,20,30]
# for i in l:
#     for j in range(1,4):
#         print(i,end=" ")
#     print()
# # 1 1 1 1
# # 2 2 2 2
# # 3 3 3 3
# l=[1,2,3]
# for i in l:
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# # another method
#
# for i in range(1,4):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#
# # 1 2 3 4
# # 1 2 3 4
# # 1 2 3 4
# for i in range(1,4):
#     for j in range(1,5):
#         print(j,end=" ")
#     print()
#
# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()
# # nested sequence
# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i,end=" ")
#     for j in i:
#             print(j,end=" ")

# # 1.give a list
# names = ['kelly', 'alan', 'jeny']
# for i in names:
#     print((name + " ") * 3)
# # 2.given a list
# # n=[1,2,3]
# n = [1, 2, 3]
# q = ['what', 'when', 'why']
# for num in n:
#     print(num)
#     print(" ".join(q))
#
# n = [1, 2, 3]
# q = ['what', 'when', 'why']
#
# for num in n:
# #     print(num)
# #     print(q[0], q[1], q[2])
# # for
# n = [1, 2, 3]
# q = ['what', 'when', 'why']
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=" ")
#     print()
#    3.
# d = [
#     {'id': 101, 'name': 'arun', 'age': 233},
#     {'id': 102, 'name': 'amal', 'age': 243},
#     {'id': 103, 'name': 'anu', 'age': 253}
# ]
#
# # print("ID NAME AGE")
# # for student in d:
# #     print(f"{student['id']} {student['name']} {student['age']}")
#
#
# d = [
#     {'id': 101, 'name': 'arun', 'age': 233},
#     {'id': 102, 'name': 'amal', 'age': 243},
#     {'id': 103, 'name': 'anu', 'age': 253}
# ]
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j)
#
# for i in range(1,4):#row
#     for j in range(1,5):#column
#         print("*",end=" ")#print
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#
# l=[23,45,78,90,12,13,91]
#
# for i in l:
#     for j in range(2, i):
#         if (i % j) == 0:
#             break
#     else:
#         print(i)

# find all prime numbers in the range(1,100)
for num in range(1, 100):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
#find all  armstrong numbers in the range(100,1000
for num in range(100, 1000):
    s = str(num)
    sum = 0
    for i in s:
        sum = sum + int(i) ** len(s)
    if sum == num:
        print(num)

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
for i in range(1,5): #outer  loop :4 lines
    for j in range(1,6): #columns
        print(j,end=" ")
    print()

#* * * *
#* * *
#**
#*
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# 1
# 2 3
# 4 5  6
# 7 8 9 10
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()

# A
# B C
# D E F
# G H I J
k=ord('A')
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
# A
# B B
# C C C
# D D D D
k=ord('A')
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(k),end=" ")
    k=k+1
    print()

# A
# A B
# A B C
# A B C D
for i in range(1,5):
    k = ord("A")
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
for i in range(1,5):
    for j in range(1,5):
        if i==j:
            print(i,end=" ")
        else:
            print(0,end=" ")
    print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0
for i in range(1,5):
    for j in range(1,i+1):
        if(j%2==0):
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
for i in range(5):
    for j in range(i+1):
        print(j,end=" ")
    print()

# h
# h e
# h e l
# h e l l
# h e l l o
s="hello"
for i in range(5):
    for j in range(i+1):
        print(s[j],end=" ")
    print()



# h
# h e
# h e l
# h e l l
# h e l l o
# h e l l o
# h e l l o   w
# h e l l o   w o
# h e l l o   w o r
# h e l l o   w o r l
# h e l l o   w o r l d
s="hello world"
for i in range(len(s)):
    for j in range(i+1):
        print(s[j],end=" ")
    print()



# *
# * *
# * * *
# * * * *
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


#      *
#     * *
#   * * *
# * * * *
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    k=k-2
    print()


#      *
#     *   *
#   *   *   *
# *   *   *   *
k=3*2
for i in range(1,5):
    for p in range(1,k+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="   ")#to increase space value
    k=k-2
    print()



k=2
for i in range(3,0,-1):
    for p in range(1,k+1):
            print("*",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")
    k=k+2
    print()
