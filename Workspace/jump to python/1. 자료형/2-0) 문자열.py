#문자열 작성
a='''Life is too short
You need python
최정선 화이팅!
'''
print(a)
#문자열 연산
a="python"
b="is fun"
print(a+b)          #python + is fun
print("*"*50)       #* 50번반복
a='life is too short, you need python'
#문자열 인덱싱& 슬라이싱
#인덱싱: a[0부터시작,반대론-1부터] 
#슬라이싱:a[이상:미만:간격]
a = "1234567890"
print(a[0])
print(a[-1])
print(a[0:4])
print(a[::2]) 

#이스케이프 코드
# %s:문자열 %c:문자 1개 %d: 정수 %f: 실수
a= "I ate %d apples. so I was %s %d days."%(23,"sick",5)
print(a)
b=23 
c="sick" 
d=5
a= "I ate %d apples. so I was %s %d days."%(b,c,d)
print(a)

#포맷함수
a= "I love {}. so I will wait {} days.".format("you",5)
print(a)
a= "I love {name}. so I will wait {day} days.".format(name="최정선",day=5)
print(a)
b="최정선"
a=f"나의 이름은 {b} 입니다."
print(a)