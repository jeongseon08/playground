#10 문자열 함수
#1. count: 문자 개수 세기
a="jeongseon"
print(a.count("e"))

#2. find: 위치 알려주기1(처음 나온 위치)
say="Don't give up, Never give up!"
print(say.find("e"))

#2.5. find: 위치 알려주기1(존재 X:-1)
say="Don't give up, Never give up!"
print(say.find("z"))

#3. index: 위치 알려주기2(처음 나온 위치)
say="Don't give up, Never give up!"
print(say.index("e"))

#3.5. index: 위치 알려주기2(존재 X:error)
say="Don't give up, Never give up!"
#print(say.index("z"))

#*4. join: 문자열 삽입
print(",".join('12345'))

#5. upper: 소문자->대문자
print("ace".upper())

#6. lower: 대문자->소문자
print("Ace".lower())

#7. lstrip: 왼쪽 공백 지우기
print("     jeongseon   ".lstrip())

#8. rstrip: 오른쪽 공백 지우기
print("     jeongseon        ".rstrip())

#9. strip: 양쪽 공백 지우기
print("     jeongseon    ".strip())

#*10. replace: 문자열 바꾸기
a="Run you clever boy, and Remeber me!"
print(a.replace("Remeber","Forget"))

#*11. split: 문자열 나누기
a="Life is too short"
print(a.split())
a,b=input().split()
print(a,b)
