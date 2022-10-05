#02 집합 종류
s1 = {1,2,3,4,5,6,7,8}
s2 = {1,2,3,9,10,11,12}

#1.교집합
print(s1&s2) 
print(s1.intersection(s2))

#2.합집합
print(s1|s2) 
print(s1.union(s2))

#차집합
print(s1-s2) 
print(s1.difference(s2))