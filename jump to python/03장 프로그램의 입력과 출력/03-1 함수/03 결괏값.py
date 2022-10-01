#03 결괏값
#1. 함수의 결괏값은 언제나 한개
#1-1. 튜플
def add_and_mul(a,b):
    return a+b,a*b
result=add_and_mul(1,5)
print(result)
#1-2. 여러개의 결괏값
result1,result2=add_and_mul(1,5)
print(result1)
print(result2)

#1-3. return 응용
def say_nick(nick):
    if nick =="바보":
        return print("넌 바보 아니야!")
    print("나의 별명은 %s 입니다." %nick)

say_nick("sunny")
say_nick("바보")
