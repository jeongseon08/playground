#피보나치 함수 선언
def fib(k):
    #첫항은 0, 두번째 항은 1
    if k==0: return 0
    if k==1: return 1
    #이전의 두항 더한 값
    return fib(k-2) +fib(k-1)

n=int(input())
#n번째 항까지 수열 출력
for i in range(n):
    print(fib(i),end=" ")

