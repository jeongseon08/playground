#10번찍어 안넘어가는 나무없다.
treehit = 0
while treehit <10:
    treehit = treehit+1 #파이썬은 treehit++가 안된다.
    print("나무를 %d 번 찍었습니다."%treehit)
    if treehit ==10:
        print("나무가 넘어갔습니다.")

#커피 자판기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee=coffee-1
    print("남은 커피의 양은%d개 입니다."%coffee)
    if not coffee:
        print("커피 재고가 떨어졌습니다.")
        break