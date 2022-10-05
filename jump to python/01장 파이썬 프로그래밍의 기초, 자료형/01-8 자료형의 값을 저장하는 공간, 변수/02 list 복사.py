#02 list 복사
#1. list 복사: 동일한 메모리 주소
a=[1,2,3,4]
b = a
print(a)
print(b)
print(id(a)==id(b))

#2. list 복사: 다른 메모리 주소
#2-1. [:]
a=[1,2,3,4]
b = a[:]
a[1]=5
print(a)
print(b)
print(id(a)==id(b))

#2-2. copy  모듈 사용
from copy import copy
a=[1,2,3,4]
b = copy(a)
c= b.copy()
a[1]=5
print(a)
print(b)
print(c)
print(id(a)==id(b))
print(id(b)==id(c))
