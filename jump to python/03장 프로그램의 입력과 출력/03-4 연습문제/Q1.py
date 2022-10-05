N=int(input("숫자를 입력하세요."))
def is_odd(N):
    if N%2==1:
        return print("홀수")
    elif N%2==0:
        return print("짝수")
is_odd(N)