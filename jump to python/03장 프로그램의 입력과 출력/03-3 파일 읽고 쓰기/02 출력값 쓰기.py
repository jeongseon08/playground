#02 출력값 쓰기
#1. w:쓰기모드
f=open("C:/Users/wjdtj/OneDrive - 강원대학교/code/playground/jump to python/03장 프로그램의 입력과 출력/03-3 파일 읽고 쓰기/new file.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
