#01 함수의 구조
#1. 함수의 구조
def add(a,b):
    print("%d+%d의 결과값을 출력합니다."%(a,b))
    return a+b
print(add(1,4))

#2. 입력값이 없는 함수
def say():
    return 'Hi'
print(say())

#3. 결괏값이 없는 함수
def add(a,b):
    print("%d,%d의 합은 %d 입니다."%(a,b,a+b))
add(3,6)
print(add(1,9))

#4. 입력, 결괏값이 없는 함수
def say():
    print("Hello")
say()
print(say())

#5. 매개변수 지정
def add(a,b):
    return a+b
result= add(b=6,a=1)
print(result)

#6. lambda
add= lambda a,b:a+b
result=add(2,7)
print(result)