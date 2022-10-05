result = 0
try:
    [1,2,3][3]
    "a"+1
    4/0
#타입 오류
except TypeError:
    result+=1

#나누기 오류
except ZeroDivisionError:
    result+=2

#리스트 인덱스 오류
except IndexError:
    result+=3
#최종값
finally:
    result+=4
print(result)