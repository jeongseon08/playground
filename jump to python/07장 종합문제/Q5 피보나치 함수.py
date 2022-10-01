def fib(k):
    if k==0: return 0
    if k==1: return 1
    return fib(k-2) +fib(k-1)

n=int(input())
for i in range(n):
    print(fib(i),end=" ")

