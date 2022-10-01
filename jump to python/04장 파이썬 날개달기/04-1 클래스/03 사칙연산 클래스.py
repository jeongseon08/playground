#03 사칙연산 클래스
#클래스 정의
class FourCal:
    #setdata(객체,매개변수)
    #메소드 정의
    def setdata(self,first,second):
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

a=FourCal()
a.setdata(9,3)
print(type(a))
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

b=FourCal()
b.setdata(6,3)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
