#include<stdio.h>
void main()
{
int a,b;
b=0;
a=1;
do
{
	b=b+a;
	printf("a\%d,b=%d\n",a,b);
a++;
}
while(a<=100);//조건식 반드식 끝에 ;을 붙인다.
printf("총합=%d,최종a=%d\n",b,a);
}