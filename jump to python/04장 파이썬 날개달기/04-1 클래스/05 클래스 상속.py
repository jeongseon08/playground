#05 클래스 상속
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

#1. 상속(Inheritance)
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result

a=MoreFourCal(8,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())