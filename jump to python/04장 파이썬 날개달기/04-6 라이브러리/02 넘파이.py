#01 넘파이
#1.넘파이 가져오기
import numpy as np

#2. 배열 생성
x=np.array([1.0,2.0,3.0])
print(x,type(x))

#3. 산술 연산 
x=np.array([1.0,2.0,3.0])
y=np.array([2.0,4.0,6.0])
print("3. x+y")
print(x+y)
print("3. x-y")
print(x-y)
print("3. x*y")
print(x*y)
print("3. x/y")
print(x/y)
print("3. y/2")
print(y/2)

#4. N차원 배열
A=np.array([[1,2],[3,4]])
print(A)
print(A.shape)

B=np.array([[3,0],[0,6]])
print("4. A+B")
print(A+B)
print("4. A*B")
print(A*B)

#5. 브로드캐스트
A=np.array([[1,2],[3,4]])
B=np.array([[10,20]])
print("5. A*B")
print(A*B)

#6. 원소접근
X=np.array([[51,55],[14,19],[0,4]])
print(X)
#6-1. 행
print(X[0])

#6-2. 행과열
print(X[1][1])

#6-3. 평탄화
print(X.flatten())

#6-4. 조건 만족값
print(X[X>15])
