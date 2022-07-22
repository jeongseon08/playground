//최정선79-함수를 이용한 구구단 프로그램
#include <stdio.h>
void gugu(int); //(2)함수선언부, 매개변수가 정수1개
void main()
{
int a; //정수형 변수선언, 지역변수
printf("원하는 단수를 입력하십시오:");
scanf("%d",&a); //표준입력함수
gugu(a); //(1)함수호출부, 매개변수1개를 값으로 전달 (Call By Value)
}
void gugu(int kk) //(3)함수정의부, main()함수에서 gugu()함수를 호출할때 매개변수 1개를 정수형으로 전달하므로 이를 받기위한 정수형변수를 선언한다.'
{
int a; //지역변수이므로 main()함수에서 선언된 정수형 변수 a와 이름이 동일하더라도 다른 변수로 인식된다.
for(a=1; a<=9; a++)
	printf("%dX%d=%d\n",kk,a,kk*a);
}