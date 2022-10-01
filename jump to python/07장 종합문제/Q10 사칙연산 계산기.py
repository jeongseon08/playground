class Calculator():
    #클래스 초기화, 생성자
    def __init__(self,numberList):
        self.numberList = numberList
    #합계
    def sum(self):
        result=0
        for num in self.numberList:
            result+=num
        return result
    #평균
    def avg(self):
        total=self.sum()
        result=total/len(self.numberList)
        return result

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())