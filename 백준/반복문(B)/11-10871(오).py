N,X=map(int,input().split()) #정수N개, 정수 X
A=list(map(int,input().split()))#수열A 리스트 값
for i in range(0,N):#N까지 반복
    if A[i] < X:
        print(A[i], end=" ")