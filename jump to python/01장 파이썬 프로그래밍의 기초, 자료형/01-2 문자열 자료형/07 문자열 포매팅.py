#07 문자열 포매팅
#1. 숫자 바로 대입
print("I eat %d apple."%3)

#2. 문자열 바로 대입
print("I eat %s apple."%"five")

#3. 숫자값 변수 대입
number=1
print("I eat %d apple." %number)

#4. 2개 이상의 값 넣기
age=26
name="최정선"
print("이름: %s 나이: %d" %(name, age))

#5. % 표현방법
#print("Error is %d%." %98)
print("Error is %d%%." %98)

#6. 정렬과 공백
#6-1. 오른쪽 정렬
print("%10s" %"hi")

#6-2. 왼쪽 정렬
print("%-10s jeongseon." %"hi")

#7. 소수점 표현
print("%0.4f"%3.4213512) #소수점 네 번째 자리까지 표현
print("%10.4f"%3.4213512) #오른쪽 정리, 소수점 표현