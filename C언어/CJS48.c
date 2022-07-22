//최정선-중첩for문 연습
#include <stdio.h>
void main()
{
int a,b;
for(a=1;a<=2;a++) //바깥 for문-행
	for(b=1;b<=3;b++) //안쪽 for 문-열
		printf("a=%d,b=%d,\n",a,b);
printf("프로그램 종료\n");
}