#02 문자열 작성 방법2
#1. 문자열에 작은 따옴표(') 포함시키기
drama= "Jeongseon's favorite drama is doctorwho"
print(drama)

#2. 문자열에 큰 따옴표(") 포함시키기
say='"Never be cruel. Never be cowardly. Never give up. Never give in."'
print(say)

#3. escape code
#3-1. 작은 따옴표(\')
fruit= 'Jeongseon \'s favorite fruit is apple'
print(fruit)

#3-2. 큰 따옴표(\")
say="\"My favorite fruit is apple.\""
print(say)

#3-3. 줄바꿈 (\n)
print("hello!\nLet me introduce myself.")

#3-4. 탭 간격(\t)
print("My name is jeongseon\tNice to meet you!")

#4. 연속된 작은 따옴표, 큰 따옴표로 둘러싸기
print('''Life is too short,
You need python!''')
print("""안녕하세요.
제 이름은 최정선입니다.
열심히 하겠습니다!""")