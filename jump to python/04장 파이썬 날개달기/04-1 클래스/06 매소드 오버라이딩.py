#06 메소드 오버라이딩
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

#1. 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

a=SafeFourCal(8,0)
print(a.div())