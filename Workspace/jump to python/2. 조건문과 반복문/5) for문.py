test_list =['one','two','three']
for i in test_list:
    print(i)

a=[(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first+last)

#당신의 결과를 알려주세요!
a=[50,25,60,45,80,75,100]
number=0
for test in a:
    number=number+1
    if test>60:
        print("%d번은 합격"%number)
    else:
        print("%d번은 불합격"%number)

#range함수(이상,미만)
sum=0
for i in range(1,11):
    sum=sum+i
print(sum)

#구구단
n=1
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ") #줄바꿈 안함(end)
    n=n+1
    print('%d단'%n)

#리스트 내포(list comprehension)
result =[num*3 for num in a if num % 2 ==0]
print(result)

result=[]
for num in a:
    if num%2==0:
        
        result.append(num*3)
        print(result)
    print(result)