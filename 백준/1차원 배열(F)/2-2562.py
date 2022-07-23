numbers=[] #빈 리스트 정의
for i in range(9):#9개 입력
    a=int(input())
    numbers.append(a) #a값을 numbers리스트에 넣는다(append)
print(max(numbers))
print(numbers.index(max(numbers))+1)