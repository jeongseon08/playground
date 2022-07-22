//최정선 **구구단 계산
#include<stdio.h>
void main()
{
int a,b,c;
for(a=1;a<=16;a++)//바깥 for문-딘수
{
	for(b=1;b<=9;b=b+1) //안쪽 for문-곱해지는수
	{
	c=a*b;
	printf("%2dx%2d=%3d\n",a,b,c);
	}
	printf("\n");
}
	printf("프로그램 종료,\n");
}