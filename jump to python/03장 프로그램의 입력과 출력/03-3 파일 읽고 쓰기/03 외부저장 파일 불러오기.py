#03 외부저장 파일 불러오기
#1.r:읽기모드
#1-1. readline 
f=open("C:/Users/wjdtj/OneDrive - 강원대학교/code/playground/jump to python/03장 프로그램의 입력과 출력/03-3 파일 읽고 쓰기/new file.txt",'r')
print("readline")
while 1:
    line=f.readline().strip() #.strip()줄끝에 \n제거
    if not line: break
    print(line)
f.close()

#1-2. readlines
f=open("C:/Users/wjdtj/OneDrive - 강원대학교/code/playground/jump to python/03장 프로그램의 입력과 출력/03-3 파일 읽고 쓰기/new file.txt",'r')
lines = f.readlines()
print("readlines")
for line in lines:
    line=line.strip()
    print(line)
f.close()

#1-3. read
f=open("C:/Users/wjdtj/OneDrive - 강원대학교/code/playground/jump to python/03장 프로그램의 입력과 출력/03-3 파일 읽고 쓰기/new file.txt",'r')
data=f.read()
print("read")
print(data)
f.close()