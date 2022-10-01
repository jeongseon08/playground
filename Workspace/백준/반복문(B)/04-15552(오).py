import sys #sys 모듈 불러오기

x = int(sys.stdin.readline().rstrip())

for i in range(x):
    A,B = map(int, sys.stdin.readline().rstrip().split())
    print(A+B)
