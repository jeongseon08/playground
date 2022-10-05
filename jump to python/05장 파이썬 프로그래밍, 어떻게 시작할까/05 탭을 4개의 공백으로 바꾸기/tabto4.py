import sys
#변수
src=sys.argv[1]
dst=sys.argv[2]
#a.txt 내용 불러오기
f=open(src)
tab_content=f.read()
f.close()
#replace함수를 통해 \t수정
space_content=tab_content.replace("\t",' '*4)
#변경사항 저장
f=open(dst,'w')
f.write(space_content)
f.close()