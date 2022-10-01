#03 오류 회피하기
try:
  f=open("null file",'r')
except FileNotFoundError:
  pass