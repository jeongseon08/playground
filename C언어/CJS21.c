//최정선21**-LEft shift 연산자(비트 연산자)
#include<stdio.h>
void main()
{
int a; //정수형변수선언
a=78; //변수 초기화
printf("%d를 좌로 1만큼 시프트=>%d\n",a,a<<1);
//LEFT shift 연산자는 우측에 있는수만큼 좌로 이동하는데, 실제로는 2^1을 곱해주는 것과 같다.
printf("%d를 좌로 2만큼 시프트 =>%d\n",a,a<<2);
}