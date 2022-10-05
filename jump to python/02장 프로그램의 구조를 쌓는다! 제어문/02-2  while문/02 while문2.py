#02 while문2
#1. Continue: while문 처음으로 이동
#1-1. Continue 사용 X
a=0
while a<10:
    if a%2==0:
        a=a+1
    else:
        print(a)
        a=a+1

#1-2. Continue 사용
a=0
while a <10:
    a=a+1
    if a%2==0: continue
    print(a)
        
#2. break
seat = 50
while seat !=0:
    money =int(input("입장료를 지불하세요."))
    
    if money >10000:
        seat=seat-1
        print('입장하시면 됩니다.')        
        print(f"거스름돈은{money-10000}원 입니다. 감사합니다.")
    
    elif money ==10000:
        seat=seat-1
        print('입장하시면 됩니다.')        

    elif money == 1:
        break

    else: print("잔액이 부족합니다.")


    if seat ==0:
        print("죄송합니다. 만석입니다.")
        break
    else:
        print(f'남은 좌석은{seat}개 입니다.')

#3. 무한loop
while True:
    print("ctrl+c를 눌러야 while문이 종료됩니다.")
    
