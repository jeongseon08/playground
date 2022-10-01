#02 비교 연산자
money=20000
#1. x<y: x가 y보다 작다
if money < 15000:
    print("오늘 저녁은 컵라면이다.")
else:
    print("오늘 저녁은 치킨이다!")

#2. x>y: x가 y보다 크다
if money > 15000:
    print("오늘 저녁은 치킨이다!")
else:
    print("오늘 저녁은 컵라면이다!")

#3. x==y: x와 y는 같다.
man = "jeongseon"
if man == "jeongseon":
    print("그 남자는 최정선이다.")
else:
    print("그는 누구지?")

#4. x!=y: x와 y는 같지 않다.
if man != "jeongseon":
    print("그는 누구지?")
else:
    print("그 남자는 최정선이다.")

#5. x<=y: x는 y보다 작거나 같다.
if money <= 15000:
    print("오늘 저녁은 컵라면이다.")
else:
    print("오늘 저녁은 치킨이다!")

#6. x>=y: x는 y보다 크거나 같다.
if money >= 15000:
    print("오늘 저녁은 치킨이다!")
else:
    print("오늘 저녁은 컵라면이다.")