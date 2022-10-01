#and(&) or(|) not in(리스트일때 사용가능)
a=[1,2,3]
b=1
if a and b:
    print("택시타")
else:
    print("걸어가")

if a or b:
    print("택시타")
else:
    print("걸어가")


if not a:
    print("택시타")
else:
    print("걸어가")

if 1 in a:
    print("택시타")
else:
    print("걸어가")

if 1 not in a:
    print("택시타")
else:
    print("걸어가")
