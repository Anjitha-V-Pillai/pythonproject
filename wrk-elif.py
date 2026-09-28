# #write a prgm to print the number of days in a month
#
# month = input("Enter month: ")
#
# l1 = ['january', 'march', 'may', 'july', 'august', 'october', 'december']
# l2 = ['april', 'june', 'september', 'november']
# l3 = ['february']
#
# if month in l1:
#     print("31 days")
# elif month in l2:
#     print("30 days")
# elif month in l3:
#     print("28 or 29 days")
# else:
#     print("Invalid")

#write a prgm to print the grades based on the following
# 91–100 → Grade A
# 81–90 → Grade B
# 71–80 → Grade C
# 61–70 → Grade D
# Below 61 → Grade E


mark=int(input("enter the mark: "))
if mark>=91 and mark<=100:
    print("Grade A")
elif mark>=81 and mark<=90:
    print("Grade B")
elif mark>=71 and mark<=80:
    print("Grade C")
elif mark>=61 and mark<=70:
    print("Grade D")
elif mark >= 0 and mark < 61:
    print("Grade E")
else:
    print("Invalid mark")