#02. 입력값
#1. *매개변수
def add_many(*arg):
    result=0
    for i in arg:
        result = result+i
    return result
print(add_many(1,2,3,4,5,6,7))

#2. 매개변수,*매개변수
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args:
            result=result+i
    elif choice =="mul":
        result=1
        for i in args:
            result=result*i
    return result
print(add_mul("add",1,2,3,4,5,6,7))
print(add_mul("mul",1,2,3,4,5,6,7))

#3. 키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=1)
print_kwargs(name='jeongseon', age=26)
