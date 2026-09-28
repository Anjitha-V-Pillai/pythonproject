l=[23,45,67,12,89,70]
print(list(filter(lambda x:x>50,l)))

colors=['red','green','blue','yellow','orange']
print(list(filter(lambda x:len (x)>5,colors)))

print(list(filter(lambda x:"n" in x,colors)))
