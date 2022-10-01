n=input() #입력갯수받는 역할, 영향력은 없다.
A=list(map(int,input().split())) #n개의 입력 정수값들 받아서 리스트화
print(min(A), max(A)) #내장함수를 이용해 최솟값과 최댓값을 받음
