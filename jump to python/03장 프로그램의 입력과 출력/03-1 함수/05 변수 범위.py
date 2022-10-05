#05 변수 범위
#1. 매개변수는 함수밖에 못나간다.
a=1
def vartest(a):
   a=a+1
   return a
print(vartest(2))
print(a) 

#2. 함수 안에서 함수 밖의 변수를 변경
#2-1. return
a=1
def vartest(a):
   a=a+1
   return a
a=vartest(a)
print(a) 

#2-2. global(비추천)
a=1
def vartest():
   global a
   a=a+1
vartest()
print(a) 