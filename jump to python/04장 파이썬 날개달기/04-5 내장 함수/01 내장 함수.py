#01 내장함수
#1. abs:절대값
print(abs(-2213))

#2. all:반복 가능여부 (and)
print(all([1,2,3,4]))
print(all([0,1,2,3,4]))

#3. any: 반복 가능여부 (or)
print(any([0,1,2,3,4]))
print(any([0,'']))

#4. chr: 유니코드
print(chr(98))
print(chr(44032))

#5. dir: 객체 변수, 객체 함수 확인
print(dir([]))
print(dir({}))

#6. divmod: 목과 나머지 튜플
print(divmod(7 ,2)) 

#7. enumerate:자료형 인덱스 열거
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

#8. eval: 문자열 실행 결괏값
eval('1+2')
eval("'best'+'python'")

#9. filter: 참 값만 추출
#9-1. filter X
def positive(l):
    result=[]
    for i in l:
        if i>0:    
            result.append(i)
    return result
print(positive([1,-3,2,0,-5,6]))

#9-2. filter O
def positive(x):
    return x>0
print(list(filter(positive,[1,-3,2,0,-5,6])))

#10. hex: 16진수
print(hex(234))
print(hex(3))

#11. input: 입력함수
a=input()
print(a)

#12. int: 문자열 형태의 숫자 정수형으로 변환
print(int("5"))

#13. isinstance: 인스턴스,클래스 판단
class Person: pass
a=Person()
b=isinstance(a,Person)
print(b)
print(isinstance(b,Person))

#14. len: 입력값의 길이
print(len("python"))

#15. list: 자료형 리스트로 변환
a="jeongseon"
print(list(a))

#16. map: 묶어주기
a,b=map(int,input().split())

#17. max: 최댓값
a=max([1,2,3,4,5,6,7])
print(a)

#18. min: 최솟값
a=min([1,2,3,4,5,6,7])
print(a)

#19. oct: 8진수 변환
print(oct(816))
#20. open(filename, [mode]): 파일 읽기방법
#20-1. w:쓰기모드
f=open('file','w')
#20-2. r:읽기모드
f=open('file','r')
f=open('file')
#20-3. a:추가 모드
f=open('file','a')
#20-4. b:바이너리 모드
f=open('file','rb')

#21. ord: 유니코드
print(ord('a'))

#22. pow: x^y
print(pow(2,4))

#23. range: 범위
print(list(range(5)))
print(list(range(5,10)))
print(list(range(5,10,2)))

#24. round: 반올림
print(round(5.8))
print(round(5.158,2))

#25. sorted: 오름차순 정렬
a=[80,5216,1218,18961]
print(a)
print(sorted(a))

#26. str:문자열 변환
a=str(85123)
print(type(a))

#27. sum: 리스트, 튜플 합
print(sum([1,2,3,4,5]))

#28. tuple: 튜플형태로 변환
a=[80,5216,1218,18961]
print(tuple(a))

#29. type: 자료형 확인
print(type(513))

#30. zip: 동일한 개수로 이뤄진 자료형 묶기
print(list(zip([1,2,3],[4,5,6])))