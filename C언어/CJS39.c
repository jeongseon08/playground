//최정선 *39-1~100 합계산
#include<stdio.h>
void main()
{
	int a,b; //정수형변수선언
 b=0; //누적합을 저장할 변수를 0으로 초기화
	for(a=1;a<=100;a=a+1)
	{
			b=b+a;
}
printf("1에서100까지의 합: %d\n",b);
}

