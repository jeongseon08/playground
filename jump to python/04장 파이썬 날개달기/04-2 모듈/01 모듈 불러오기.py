#01 모듈 불러오기
#1. import
import mod1
print(mod1.add(3,5))

#2. from import
from mod1 import add
print(add(3,6))

#3. from import *
from mod1 import *
print(add(3,7))

#4. if __name__=="__main__":의 의미
#4-1. if __name(X)
import mod2
print(mod2.add(4,2))

#2. if __name(O)
import mod3
print(mod3.add(4,2))
