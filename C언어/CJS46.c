//최정선46-키보드로부터 입력받은 값으로 합 계산
#include<stdio.h>
void main()
{
int a,b,c,d,e; //정수형변수선언
 e=0; //누적합을 저장할 변수를 0으로 초기화
 printf("초기값,최종값,증감값을 입력하십시오:");
	scanf("%d%d%d",&b,&c,&d);
	for(a=b;a<=c;a=a+d)
			e=e+a;
printf("초기값=%d,최종값=%d,증감값=%d\n",b,c,d);
printf("%d부터 %d까지 %d씩 증가하여 누적된 값 : %d\n",b,c,d,e);
}

