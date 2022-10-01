#append(추가)/reverse(역순)/sort(정렬-오름차순)/insert(인덱스위치에 추가)/
a=["최정선","조해준","지현근"]
a.append("박재균") #리스트 마지막에 추가하는 함수
print(a)
a.reverse() #리스트의 순서 반대로 배치하는 함수
print(a)
a.sort()    #리스트 자료 오름차순 정리해주는 함수
print(a)
a.insert(2,"윤일주") #인덱스위치에 자료 추가하는 함수
print(a)
a.remove((a[2])) #값을 제거하는 함수
print(a)
print(a.pop()) #마지막 자료 꺼내는 함수
print(a.count("최정선"))#자료안에 해당 문자열 몇개인지 카운트해주는 함수
a.extend(["윤일주","최정선"]) #리스트를 추가해주는 함수
print(a)