#01 정규표현식
#1. 주민번호 뒷자리 모자이크(정규식 X)
data='''park 800905-1049118,choi 700905-1059119'''
result=[]
#data를 ,기준으로 나눈다.
for line in data.split(","):
    word_result=[]
    #이름과 주민번호 나눈다.
    for word in line.split(" "):
        #문자열 내용 주민번호 여부 확인(길이:14, -[6]제외하고 숫자인지 확인)
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+"-"+'*******'
        word_result.append(word)
        #리스트에 결과 넣기
    result.append("".join(word_result))
    #리스트 요소 문자열로 합치기
print("\n".join(result))

#2. 주민번호 뒷자리 모자이크(정규식 O)
import re
data='''park 800905-1049118
choi 700905-1059119'''
pat=re.compile('(\d{6})[-]\d{7}')
print(pat.sub("\g<1>-*******",data))