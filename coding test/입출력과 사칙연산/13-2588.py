A,B=int(input().split())
print(A*(B%10))
print(A*(B%100/10))
print(A*(B/100))
print(A*B)
#위의 예문은 런타임 오류
#런타임을 준수하자.
A=int(input())
B=input()
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))
