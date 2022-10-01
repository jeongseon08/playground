#07 클래스 변수
#1. 클래스 변수
class Family:
    lastname="김"
#2.객체 변수
a=Family()
b=Family()
print(a.lastname)
print(b.lastname)

#3. 클래스 변수 변경
Family.lastname="최"
print(a.lastname)
print(b.lastname)
#4. 객체변수 변경
a.lastname="이"
print(a.lastname)
print(b.lastname)
