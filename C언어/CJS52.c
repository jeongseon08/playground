#include<stdio.h>
void main()
{
int a,b; //정수형 변수선언
b=0;
a=1; //반복용 변수 초기값
while(a<=100) //조건식
{
b=b+a;
a++;
} //while용
printf("총합=%d\n",b);
printf("최종=%d\n",a);
}