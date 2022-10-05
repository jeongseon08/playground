#01 구구단
#1. 반복문 X
n=int(input())

def gugu1(n):
    result=[]    
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result
print(gugu1(n))

#2. while
def gugu2(n):
    result=[]    
    i=1
    while i <10:
        result.append(n*i)
        i=i+1
    return result
print(gugu2(n))

#3. for
def gugu3(n):
    result=[]    
    i=1
    for i in range(1,10):
        result.append(n*i)
    return result
print(gugu3(n))
