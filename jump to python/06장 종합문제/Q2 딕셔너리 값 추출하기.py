try:
  a={'A':90,'B':80}
  #a 딕셔너리에는 ['C']가 없으므로 오류가 발생한다.
  a['C']
  #오류 발생시 70을 출력
except KeyError:
  print(70)