//최정선40**-특정값부터 100 까지의 합 계산
#include<stdio.h>
void main()
{
	int a; //반복문을 위한 정수형 변수선언
	int b; //누적합을 저장할 정수형 변수선언
 b=0; //누적합을 저장할 변수를 0으로 초기화
for(a=37;a<=1000;a++)
{
b=b+a;
printf("a=%d\n",a);
}//반복할 문장이 2개 이상일떄는 {}로 묶어줍니다.
printf("최종합:%d, 최종a=%d\n",b,a);
b=0;
for(a=45;a<501;a=a+2)
	b+=a;
printf("최종합=%d,최종a=%d\n",b,a);
}