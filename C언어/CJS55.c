//최정선 55-break문을 활용한 루프탈출 예제
#include <stdio.h>
void main()
{
int a,b;
b=0;
for(a=1;a<=1000;a++)
{ //for문에 실행할 문장이 2개이상일 경우에는 중괄호로 묶는다.
	b=b+a;
	printf("a=%d,누적합=%d\n",a,b);
	if(b>=1000) //누적합이 1000이상일경우
		break;
}
printf("최종");
}