a=[1,2,3]
print(id(a))
a=a+[4,5]
#a를 새롭게 정의했으므로 주소값이 달라진다.
print(id(a))

a=[1,2,3]
print(id(a))
#a에 요소를 추가한 것으로 주소값은 변하지 않는다.
a.extend([4,5])
print(id(a))