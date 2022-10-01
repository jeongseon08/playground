H,M= map(int,input().split())
T=int(input())
if M+T >59:
    H=H+((M+T)//60)
    if H>=24:
        H=H-24
    M=(M+T)%60
    print(H,M)
else:
    M=M+T
    print(H,M)