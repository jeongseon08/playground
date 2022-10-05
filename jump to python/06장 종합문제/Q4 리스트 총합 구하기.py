A=[20,55,67,82,45,33,90,87,100,25]
#1. for
result=0
#A점수 합산하기
for mark in A:
    #50점 이상
    if mark>=50:
        #결과값에 더하기
        result+=mark
print(result)

#2. while
result=0
while A:
    mark=A.pop()
    if mark>=50:
        result +=mark
print(result)