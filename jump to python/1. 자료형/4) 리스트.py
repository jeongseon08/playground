a=["최정선","조해준","지현근",["a","b","c","d"]]
print(a[3])
print(a[3][1])
print(a[0]+a[1])
print(a[0:3])
a[1]="윤일주"
print(a)
a[1:3]= "박재균","윤일주"
print(a)
a[2:3]=[]
print(a)
del a[1]
print(a)