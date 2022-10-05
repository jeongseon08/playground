#06 리스트 함수
a=["최정선",26,"인천"]
b=[1,9,6,4,2]
c=["e",'b','a','z','c']

#1. append: 리스트에 요소 추가
a.append("010-4935-4629")
print(a)

#2. sort: 리스트 정렬
b.sort()
c.sort()
print(b)
print(c)

#3. reverse: 리스트 뒤집기
b.reverse()
c.reverse()
print(b)
print(c)

#4. index: 위치 반환
print(a.index(26))
print(b.index(2))
print(c.index("c"))

#5. insert: 리스트에 요소 삽입(원하는 위치)
a.insert(3,"ttt2113@naver.com")
print(a)

#6. remove: 리스트 요소 제거
a.remove(26)
print(a)

#7. pop: 리스트 요소 끄집어내기
number=a.pop(-1)
print(number)
print(a)

#8. count: 리스트에 포함된 요소 x의 개수 세기
num=[1,2,3,4,5,6,1,2,3,2,1,1,1,7]
print(num.count(1))

#9. extend: 리스트 확장(리스트+리스트)
a=["최정선",26,"인천"]
a.extend(["010-4935-4629","ttt2113@naver.com"])
print(a)
b=["최정선",26,"인천"]
c=["010-4935-4629","ttt2113@naver.com"]
print(b+c)
