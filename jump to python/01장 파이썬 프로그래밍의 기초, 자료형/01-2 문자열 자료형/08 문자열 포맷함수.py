#08 문자열 포맷함수
#1. 숫자 바로 대입
a="I eat {0} apples.".format(4)
print(a)

#2. 문자열 바로 대입
print("I eat {0} apple.".format("five"))

#3. 숫자값 변수 대입
number=1
print("I eat {0} apple.".format(number))

#4. 2개 이상의 값 넣기
name="최정선"
age=26
#4-1. 인덱스
print("이름: {0} 나이: {1}".format(name,age))

#4-2. 변수명 
name="최정선"
age=26
print("이름: {name} 나이: {age}".format(name="최정선",age=26))

#4-3. 인덱스와 변수명
print("이름: {0} 나이: {age}".format("최정선",age=26))

#5. 정렬과 공백
#5-1. 왼쪽 정렬
print("{0:<10}".format("Jeong"))

#5-2. 오른쪽 정렬
print("{0:>10}".format("seon"))

#5-3. 가운데 정렬
print("{0:^10}".format("jeongseon"))

#5-4. 공백 채우기
print("{0:*^9}".format("hello"))
print("{0:#<15}".format("jeongseon"))

#6. 소수점 표현
pi=3.141592
print("{0:0.2f}".format(pi))
print("{0:10.2f}".format(pi))

#7. { 또는 } 문자 표현하기
a="{{and}}".format()
print(a)