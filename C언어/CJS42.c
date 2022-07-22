//최정선42-1~100 홀수와 짝수합의 계산
#include<stdio.h>
void main()
{
int a,b;
b=0; //홀수합을 저장할 변수 초기화
for(a=1;a<=100;a=a+2)
	b=b+a; //누적식
printf("1부터 100까지의 홀수 합=%d\n",b);
b=0;
for(a=0;a<=100;a=a+2)
	b+=a; //누적식
printf("1부터 100까지의 짝수 합=%d\n",b);
}