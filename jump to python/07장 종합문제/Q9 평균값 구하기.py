f=open("C:/code/playground/jump to python/07장 종합문제/sample.txt",'r')
rank=f.read()
f.close()

rank=rank.split("\n")
result=0
for i in rank:
    i=int(i)
    result=result+i
avr=result/len(rank)

f=open("C:/code/playground/jump to python/07장 종합문제/result.txt",'w')
f.write(str(avr))
f.close()