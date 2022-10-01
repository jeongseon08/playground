#01 while문
#1. while문 기본 구조
treeHit = 0
while treeHit <10:
    treeHit=treeHit+1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit ==10:
        print('나무 넘어갑니다.')

#2. while문 활용법
number=0
prompt='''
1. Add
2. Del
3. List
4. Quit
Enter number:'''

while number !=4:
    print(prompt)
    number=int(input())