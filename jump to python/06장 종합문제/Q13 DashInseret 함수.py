data=input()
numbers=list(map(int,data))
result=[]
y=0
#enumerate:리스트 인덱스 자동생성
for i,num in enumerate(numbers):
    result.append(str(num))
    #마지막 숫자는 추가할 필요 없으므로 다음 수 유무 조건문
    if i<len(numbers)-1:

        #홀수 판단
        is_odd=num%2==1
        is_next_odd=numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append("-")
        
        #짝수
        elif not is_odd and not is_next_odd:
            result.append("*")

print(" ".join(result))