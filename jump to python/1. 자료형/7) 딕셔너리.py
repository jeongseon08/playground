dic = {'name':'Eric','age':15}
print(dic['name'])
dic['tall']="170cm" #딕셔너리 추가
print(dic)
del dic['name'] #딕셔너리 삭제
print(dic)
#keys 키 추출하는 함수, values 변수 추출하는 함수, item 각 쌍끼리 담는 함수, get 값 찾아주는 함수, in 변수안에 키찾기(T or F)
dic = {'name':'Eric','age':15,'tall':"170cm"}
print(dic.keys()) #키추출
print(dic.values()) #변수 추출
print(dic.items()) # 쌍(키,변수)으로 추출
print(dic.get(2,"없다고!")) #해당 값 찾기, 없을땐 default:None "없다고!"
print("name" in dic) #키가 변수안에 있나요?