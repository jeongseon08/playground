f=open("C:/code/playground/jump to python/07장 종합문제/abc.txt","r")
text=f.read()
f.close()
#txt파일 내용 불러오기
text=text.split("\n")
#역순
text.reverse()
f=open("C:/code/playground/jump to python/07장 종합문제/abc.txt","w")
#역순으로 작성한 내용 저장
for i in  text:
    f.write(i)
    f.write("\n")
f.close()
