#04 생성자
#1. Constructor: __init__

class FourCal:
    #메소드 정의
    def __init__(self,first,second):
        self.first=first
        self.second=second
    #덧셈 기능
    def add(self):
        result=self.first+self.second
        return result
    #곱셈 기능
    def mul(self):
        result=self.first*self.second
        return result
    #뺄셈 기능
    def sub(self):
        result=self.first-self.second
        return result
    #나눗셈 기능
    def div(self):
        result=self.first/self.second
        return result

a=FourCal(8,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

i1,i2=map(int,input("계산할 값을 입력하세요.").split())
b=FourCal(i1,i2)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
