#04 in, not in
info=["jeongseon",'010-4935-4629','ttt2113@naver.com']
data=input('data:')
#1. in
if data in info:
    print("data check complete")
else:
    print('error')

#2. not in

if data not in info:
    print("error")
else:
    print('data check complete')