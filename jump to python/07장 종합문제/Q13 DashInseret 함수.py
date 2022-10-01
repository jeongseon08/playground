data=input()
data=list(data)
result=[]
y=0
for i in data:
    i=int(i)
    y=i
    result.append(i)
    if y%2==0:
        result.append(i)
        if i%2==0:
            result.append("*")
    elif i%2==1:
        result.append(i)
        if i%2==1:
            result.append("-")
print(result)