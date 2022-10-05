import sys
#sys.argv: 명령행에서 인수 전달
numbers = sys.argv[1:] #[1:]를 통해 파일명 제외한 명령 행의 모든 입력
result = 0
for number in numbers:
    result += int(number)
print(result)
