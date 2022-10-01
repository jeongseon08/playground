a=[1,2,3]
print(id(a))
a=a+[4,5]
print(id(a))

a=[1,2,3]
print(id(a))
a.extend([4,5])
print(id(a))