#extend함수 사용
a=[]
a.extend(map(int,input().split(",")))
print(a)
#내장함수 sum사용하기
print(sum(a))

#for문 사용
user_input=input("숫자를 입력하세요:")
numbers=user_input.split(",")
print(numbers)
total=0
for n in numbers:
    total+=int(n)
print(total)