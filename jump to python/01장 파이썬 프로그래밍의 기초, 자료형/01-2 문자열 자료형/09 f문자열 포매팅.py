#09 f문자열 포매팅 :python3.6v
#1. f문자열 포매팅
name="최정선"
age=26
#1-1. f문자열
print(f'제 이름은 {name}입니다. 나이는 {age}입니다.')

#1-2. 정렬
print(f'{"jeong":<10}')
print(f'{"seon":>10}')
print(f'{"최정선":^10}')

#1-3. 공백 채우기
print(f'{"jeong":#<10}')
print(f'{"seon":#>10}')
print(f'{"최정선":*^10}')

#1-4. 소수점
pi=3.141592
print(f"{pi:0.2f}".format(pi))
print(f"{pi:10.2f}".format(pi))

#1-5. { 또는 } 문자 표현하기
a=f"{{or}}"
print(a)

#2. 딕셔너리 f문자열 포매팅
d={'name':'최정선','age':26}
print(f'제 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')
