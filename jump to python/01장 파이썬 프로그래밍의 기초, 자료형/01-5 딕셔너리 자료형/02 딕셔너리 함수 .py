#02 딕셔너리 함수
info = {'name':'jeongseon','age':26, 'phone':'010-4935-4629'}

#1. 딕셔너리 쌍 추가하기
info['e-mail']='ttt2113@naver.com'
info['sex']='male'
print(info)
#2. 딕셔너리 요소 삭제하기
del info['phone']
print(info)

#3. keys: key list
#3-1. dic_keys 리스트
print(info.keys())

#3-2. dic_keys 활용: list함수 Error
for k in info.keys():
    print(k)

#3-3. list
print(list(info.keys()))

#4. values: value list
print(info.values())

#5. items: key& values 쌍 얻기(튜플)
print(info.items())

#6. clear: key7 values 쌍 모두 지우기
info.clear()
print(info)

#7. get: key로 value 얻기
info = {'name':'jeongseon','age':26, 'phone':'010-4935-4629'}
print(info.get('name'))
print(info.get('age'))
print(info.get('phone'))
print(info.get('sex'))
print(info.get('sex','I don\'t know'))

#8. in: 해당 key가 딕셔너리 안에 있는지 조사
print('name' in info)
print('sex' in info)