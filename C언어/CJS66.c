//최정선66**-사용자정의함수#2
#include <stdio.h>
void abc();//함수선언부, 함수는 호출되기전에 반드시 선언되어야한다. main()함수앞에
int xyz();
void main()
{
int s;
printf("현재 main()함수에 있음\n");
abc(); //사용자정의함수 , 함수호출부
printf("다시 main()함수로 돌아옴\n");
s=xyz(); //리턴값을 변수s에 대입하는 함수 호출부
printf("함수 xyz()로부터 리턴값은 %d\n",s);
}
void abc() //함수 정의부
{
printf("안녕하세요.\n");
printf("반갑습니다.\n");
}	
int xyz() //함수정의부, 함수선언부와 동일한 함수 의 형 (int)으로정의 해준다.
{
printf("xyz()함수에 있음\n");
return 777; //호출된 함수정의부에 return문장이있으면 옆에 나오는 변수또는 값을 호출된 곳으로 돌려준다.

}