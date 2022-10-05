#06 문자열 나누기
a = "20010331Rainy"

#1. 문자열 3구간으로 나누기
year = a[:4]
day = a[4:8]
weather = a[8:]
print("year:",year)
print("day:",day)
print("weather:",weather)
print(year,day,weather)

#2. 문자열 수정(Error)
a = "Pithon"
a[:1]='y' 
#Solution: 문자열의 요솟값은 바꿀 수 있는 값이 아니기 때문이다.
# 문자열자료형은 그 요솟값을 변경할 수 없다. 그래서 immutable한 자료형이라고도 부른다.

#3. 문자열 수정(Error 수정)
print(a)
print(a[:1]+'y'+a[2:])