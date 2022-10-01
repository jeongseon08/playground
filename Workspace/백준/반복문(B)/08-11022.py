#풀이 1. 이스케이프 코드 사용
t=int(input())
for i in range(1,t+1):
   a,b=map(int,input().split())
   print("Case #%d: %d + %d = %d"%(i,a,b,a+b))

#풀이 2. 포맷함수 사용
t=int(input())
for i in range(1,t+1):
    a,b=map(int,input().split())
    print("Case #{}: {} + {} = {}".format(i,a,b,a+b))