#02 오류 예외 처리 기법
#1. try,except문
try:
  ...      
except:
  ...

#2. 발생 오류만 포함한except문
try:
  ...
except FileNotFoundError:
  ...

#3. 발생 오류와 오류 메시지 변수까지 포함한 except문
#3-1. 없는 파일
try:
  f = open("null",'r')
except FileNotFoundError as e:
  print(e)

#3-2. x/0
try:
  4/0
except ZeroDivisionError as e:
  print(e)

#3-3. 없는요소
try:
  a=[1,2,3]
  a[4]
except IndexError as e:
  print(e)

#4. 여러개의 오류처리하기
#4-1. 마지막 오류만 출력됨.
try:
  a =[1,2]
  print(a[3])
  4/0
except ZeroDivisionError:
  print("0으로 나눌수 없습니다.")

except IndexError:
  print("인덱싱 할 수 없습니다.")

#4-2. 다중 오류 출력하기
try:
  a =[1,2]
  print(a[3])
  4/0
except (ZeroDivisionError,IndexError) as e:
  print(e)

#5. try문에 else절 사용
try:
  age=int(input("나이를 입력하세요:"))
except :
  print("올바르지 않은 입력값입니다.")

else:
      print("귀하의 나이는 %d입니다." %age)
      if age<=19:
            print("미성년자는 출입금지입니다.")
      else: print("환영합니다.")