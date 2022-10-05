#04 내용 추가하기
#1. a:추가모드
f=open("C:/Users/wjdtj/OneDrive - 강원대학교/code/playground/jump to python/03장 프로그램의 입력과 출력/03-3 파일 읽고 쓰기/new file.txt",'a')
for i in range(11,21):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
