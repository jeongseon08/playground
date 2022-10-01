a=[]
a.extend(map(int,input().split(",")))
print(a)
print(sum(a))

user_input=input("숫자를 입력하세요:")
numbers=user_input.split(",")
print(numbers)
total=0
for n in numbers:
    total+=int(n)
print(total)