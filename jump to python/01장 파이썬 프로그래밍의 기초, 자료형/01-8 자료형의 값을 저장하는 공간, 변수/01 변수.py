#01 변수
#1. 변수 선언
a=1
b='python'
c=[1,2,3]

#2. 변수 메모리 주소
print(id(a))
print(id(b))
print(id(c))

#3. list 복사
b = a
print(id(a))
print(id(b))
print(id(a)==id(b))