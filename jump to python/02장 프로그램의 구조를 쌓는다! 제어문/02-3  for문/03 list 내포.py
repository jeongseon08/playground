#03 list 내포
#1. list 내포X
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

#2-1. list 내포O
a=[1,2,3,4]
result=[num* 3 for num in a]
print(result)

#2-2. list 내포, if문
a=[1,2,3,4]
result=[num* 3 for num in a 
if num%2==0]
print(result)

#2-3. 구구단 리스트 내, 2개이상의 for문
result=[x*y for x in range(2,10) 
for y in range(1,10)]
print(result)