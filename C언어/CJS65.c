//최정선65*-사용자정의함수#1
#include <stdio.h>
void abc(); //함수선언부, 함수는 호출되기전에 반드시 선언되어야한다. main()함수앞에
void main()
{
printf("안녕하세요.\n");
printf("안녕하세요.\n");
printf("안녕하세요.\n");
abc(); //사용자정의함수 , 함수호출부
abc();
abc();
abc();
abc();
}
void abc() //함수정의부,main()함수앞에 선언된 사용자 정의함수는 main()함수 앞 또는 뒤에 반드시 수행해야한다.
{
printf("반갑습니다\n");
}	