import os
# 검색함수 정의
def search(dirname):
    try:
        #디렉토리에 있는 파일 리스트화
        filenames=os.listdir(dirname)
        #파일 이름 반복문
        for filename in filenames:
            #디렉토리 포함한 전체경로
            full_filename=os.path.join(dirname,filename)
            #디렉토리일 경우 해당 경로에서 search함수  호출
            if os.path.isdir(full_filename):
                #재귀호출
                search(full_filename)
        
            else:
                #파일이름과 확장자 나누기
                ext = os.path.splitext(full_filename)[-1]
                #확장자 명
                if ext=='.py':
                    print(full_filename)
#접근 권한없는 디렉토리에 의한 오류 제거
    except PermissionError:
        pass

search("C:/")