#01 딕셔너리
#1. 딕셔너리 구조: 키,변
dic1 = {'key1':'value1','key2':'value2','key3':'value3'}
print(dic1)
info = {'name':'jeongseon','age':26, 'phone':'010-4935-4629', 'favorite':['drama','movie','music','talk,']}
print(info)

#2. 딕셔너리 주의사항
#2-1. 중복된 키값
dic1 = {'key1':'value1','key1':'value2','key3':'value3'}
print(dic1)

#2-2. 리스트 키:Error
#info = {'name':'jeongseon','age':26, 'phone':'010-4935-4629', ['drama','movie','music','talk,']:'favorite'}

#3. 딕셔너리에서 key를 사용해 value 얻기
info = {'name':'jeongseon','age':26, 'phone':'010-4935-4629', 'favorite':['drama','movie','music','talk,']}
print(info['name'])
print(info['age'])
print(info['phone'])
print(info['favorite'])