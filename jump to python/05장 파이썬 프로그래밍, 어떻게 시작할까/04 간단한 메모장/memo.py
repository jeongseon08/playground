import sys
option=sys.argv[1]
#추가모드
if option=='-a':
    memo=sys.argv[2]
    f=open('memo.txt','a') #memo.txt를 추가모드로 열기
    f.write(memo) #작성
    f.write('\n')#줄바꿈
    f.close() #파일 닫기
#조회 모드(읽기모드)
elif option=='-v':
    f=open('memo.txt','r') #memo.txt를 읽기모드로 열기
    memo=f.read() #메모내용
    f.close()   
    print(memo) #메모내용 출력