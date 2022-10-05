#04 매개변수 설정
#1. 초깃값 미리 설정
def say_myself(name,old, man=True):
    print('나의 이름은 %s입니다.'%name)
    print('나의 나이는 %d입니다.'%old)
    if man:
        print("나는 남자입니다.")
    else:
        print("나는 여자입니다.")
say_myself('최정선',26)
say_myself('최정선',26,False)

