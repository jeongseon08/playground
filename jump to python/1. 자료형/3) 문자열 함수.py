#acount(갯수)/find(위치 찾기)/index(위치 찾기2)/join(삽입)/upper/lower(대문자 소문자 바꾸기)/strip(공백X)
a="hello world!"
b="<"
c="               hi            "

print(a.count("h"))     #h 몇개인지 찾아주는 함수
print(a.find("o"))      #o가 몇번째 인덱스에 있는지 찾아주는 함수
print(a.index("o"))     #o가 몇번째 인덱스에 있는지 찾아주는 함수2
print(b.join("1234"))   #b(<)를 "1234" 문자사이에 삽입하는 함수
print(a.upper())        #대문자로 바꿔주는 함수
print(a.lower())        #소문자로 바꿔주는 함수
print(c.strip())        #공백을 없애주는 함수
#replace(교체)/split(기준으로 자르기)
a= "Hello world!"
print(a.replace("world","jeongseon"))
a="a:b:c:d"
print(a.split(":"))
