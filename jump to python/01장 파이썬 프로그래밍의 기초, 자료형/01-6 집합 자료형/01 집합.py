#01 집합
#1. 집합 구조
#1-1. {}
s1 = {1,2,3,4}
print(s1,type(s1))

#1-2. set
s2 = set([1,2,3,4])
print(s2,type(s2))


#1-3. set(""): 순서는 random
s3= set("jeongseon")
print(s3,type(s3))

#1-4. list set화: 중복 요소 제거
l = [1,2,2,3,4,5,4,2,2,4,1]
print(set(l)) 
print(list(set(l)))
