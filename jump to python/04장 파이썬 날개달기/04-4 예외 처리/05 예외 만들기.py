#05 예외 만들기
#1. 예외 만들기
class MyError(Exception):
  pass

def say_nick(nick):
  if nick =="바보":
    raise MyError()
  print(nick)

try:
  say_nick("천사")
  say_nick("바보")
except MyError:
  print("허용되지 않는 별명입니다.")
  
  #2. __str__ 메소드 구현
class MyError(Exception):
      def __str__(self):
          return "허용되지 않는 별명입니다."

def say_nick(nick):
  if nick =="바보":
    raise MyError()
  print(nick)

try:
  say_nick("천사")
  say_nick("바보")
except MyError as e:
  print(e)