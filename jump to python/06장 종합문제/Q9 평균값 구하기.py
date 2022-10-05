# 저장된 값 불러오기
f=open("C:/code/playground/jump to python/07장 종합문제/sample.txt",'r')
rank=f.read()
f.close()
#줄 별로 요소 나누기
rank=rank.split("\n")
result=0
#합계
for i in rank:
    i=int(i)
    result=result+i
#평균 값
avr=result/len(rank)

f=open("C:/code/playground/jump to python/07장 종합문제/result.txt",'w')
f.write(str(avr))
f.close()