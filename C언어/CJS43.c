//최정선43-1~100 홀수와 짝수합의 계산 if문 사용
#include<stdio.h>
void main()
{
int a,b,c;
b=c=0;
for(a=1;a<=100;a++)
{
if(a%2==1)
	b=b+a;
else
	c=c+a;
}
printf("1부터 100까지의 홀수 합=%d\n",b);
printf("1부터 100까지의 짝수 합=%d\n",c);
}