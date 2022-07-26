//최정선67**-매개변수(파라미터)가 있는 사용자정의 함수 #3
#include <stdio.h>
void abc(int); //매개변수가 정수형 1개로 구성된 함수선언부, 리턴값은 없다.
void main()
{
abc(7); //매개변수 
printf("x=%d, w=%d\n",x,w); //변수w와 x는 main()함수에서 선언 되지 않았으므로 사용할수 없다.
}
void abc(int x)//정수형 매개변수가 있으므로 데이터형(int)과 호출부에서 전달될 값을 받을 변수를 지정해준다.
{
int w; //abc()함수에서만 사용될 지역변수선언
w=100;
w=w+x;
printf("변수 w=%d, x=%d\n",w,x);
}