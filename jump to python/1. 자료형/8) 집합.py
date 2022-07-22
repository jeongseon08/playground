s1 = set([1,2,3,4])
s2 = {1,2,3,4}
print(s1)
print(s2)
print(type(s1)) #type:set
l = [1,2,2,3,4,5,4,2,2,4,1]
print(list(set(l))) #리스트의 중복 요소 집합으로 제거 후 리스트화
a= set("Hello")
print(a) #출력할때마다 순서는 달라진다.
#교집합, 다른언어는 복잡합다.
s1 = {1,2,3,4,5,6,7,8}
s2 = {1,2,3,9,10,11,12}
#교집합
print(s1&s2) 
print(s1.intersection(s2))
#합집합
print(s1|s2) 
print(s1.union(s2))
#차집합
print(s1-s2) 
print(s1.difference(s2))
#원소추가
s1.add(9)
print(s1)
s1.update([1,12,13,14])
print(s1)
#원소제거
s1.remove(1)
print(s1)