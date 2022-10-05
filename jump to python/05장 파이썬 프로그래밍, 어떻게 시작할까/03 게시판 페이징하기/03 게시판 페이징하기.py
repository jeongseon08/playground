#03 게시판 페이징하기
m,n=map(int,input('게시물수와 페이지당 보여줄 수를 입력하세요.').split())

def getTotalpage(m,n):
    if m%n==0:
        return m//n
    else:
        return m//n+1
print(getTotalpage(m,n))