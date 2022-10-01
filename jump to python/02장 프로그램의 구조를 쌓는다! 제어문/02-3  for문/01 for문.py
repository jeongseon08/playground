#01 for문
#1. for문 기본 구조
data=['최정선','010-4935-4629','ttt2113@naver.com']
for i in data:
    print(i)

#2. for문 응용
#2-1. 리스트,튜플
a=[(1,3),(2,4),(3,12),(10,2)]
for (first,last) in a:
    print(first+last)

#2-2. 합격 여부
marks=[90,52,67,45,80]
number=0
for mark in marks:
    number=1+number
    if mark >60:
        print(f"{number}번 지원자는 합격입니다.")
    else:
        print(f"{number}번 지원자는 탈락입니다.")

#2-3. 합격 여부(continue)
marks=[90,52,67,45,80]
number=0
for mark in marks:
    number=1+number
    if mark < 60:continue

    print(f"축하합니다. {number}번 지원자는 합격입니다.")
    