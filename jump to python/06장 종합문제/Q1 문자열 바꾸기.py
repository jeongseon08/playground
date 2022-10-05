#1. split과 join 활용
str1="a:b:c:d"
#:를 기준으로 문자열 분리하기
str2=str1.split(":")
print(str2)
#문자열 사이에 삽입하기
str3="#".join(str2)
print(str3)

#2. replace 활용
str1="a:b:c:d"
#":"을 "#"으로 변경하기
str2=str1.replace(":","#")
print(str2)