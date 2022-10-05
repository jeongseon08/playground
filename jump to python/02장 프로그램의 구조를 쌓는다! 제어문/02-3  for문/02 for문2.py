#02 for문2
#1. range: 범위(이상,미만)
#1-1. range 기본구조
a=range(1,10)
print(a)
#1-2. 합격 여부
marks=[90,52,67,45,80]
for num in range(len(marks)):
    if marks[num] < 60:continue
    print(f"축하합니다. {num+1}번 지원자는 합격입니다.")

#1-3. 구구단1
for x in range(2,10):
    for y in range(1,10):
        print(f"{x}X{y}=",x*y,end=" ")
    print('')

#1-4. 구구단2
x=int(input())
for y in range(1,10):
    print(f"{x} X {y} =",x*y)

#2. list 내포
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)
