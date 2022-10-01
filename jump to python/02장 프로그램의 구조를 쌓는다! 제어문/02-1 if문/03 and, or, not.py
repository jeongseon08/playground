#03 and, or, not
money1,money2=map(int,input().split())
#1. and: x와 y 모두 참이어야 한다.
if money1 > 2000 and money2 > 2000 :
    print("두명 다 버스탈 수 있어.")
else:
    print("버스를 탈 수 없어.")

#2. or: x와 y 둘중에 하나만 참이어도 참이다.
if money1 > 4000 or money2 > 4000 :
    print("택시비 내가 낼게")
else:
    print("택시 타기는 힘들겠다.")

#3. not: x가 거짓이면 참이다.
man = input("이름을 입력하세요.")
if not man =="jeongseon":
    print("접근 할 수 없습니다.")
else:
    print("본인 확인됐습니다.")
