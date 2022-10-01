#01 if문
#1. if문 기본 구조
money= True
if money:
    print("오늘 저녁은 치킨이다!")
else:
    print("오늘 저녁은 굶자...")

#2. 간단 표현식
if money: print("오늘 저녁은 치킨이다!")
else: print('오늘 저녁은 굶자...')

#3. 조건부 표현식
score=int(input('점수를 입력하세요.'))
message = 'success' if score >=60 else "failure"
print(message)