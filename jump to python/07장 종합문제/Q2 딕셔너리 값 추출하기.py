a={'A':90,'B':80}
a.get('C',70)

try:
  a={'A':90,'B':80}
  a['C']
except KeyError:
  print(70)