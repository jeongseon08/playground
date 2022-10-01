#04 오류 일부러 발생시키기
#1. 오류 발생
class Bird:
  def fly(self):
    raise NotImplementedError

#2. 상속 클래스에서 fly함수 필수 구현
class Eagle(Bird):
  def fly(self):
        print("very fast")
eagle=Eagle()
eagle.fly()