//최정선35-switch~case문을 사용한 ATM기 프로그램
#include<stdio.h>
void main()
{
int a; //정수형 변수선언. 사용자가 입력한 값을 저장할 변수
printf("<1:입금, 2:출금, 3:이체, 4:통장정리>\n");
printf("원하는 메뉴를 선택하세요:");
scanf("%d",&a);
switch(a) //조건식 또는 변수
{
case 1: //a값이 1인경우,'(세미콜론);이 아니라 (콜론):'을 붙인다. case 뒤에 숫자는 뛰고 나서 작성
	printf("입금 실행\n");break; //해당문장을 실행 후에는 switch~case문을 빠져나가야한다.
case 2: printf("출금실행\n");break;
case 3: printf("이체 실행\n");break;
case 4: printf("통장 정리\n");break;
default: printf("메뉴는 1~4번사이의 정수만 가능하므로 잘못된 입력입니다.\n");break;
} //switch-case문의 집합
printf("프로그램을 종료하겠습니다.\n");
} //main()함수의 집합