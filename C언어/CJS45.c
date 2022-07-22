#include<stdio.h>
void main()
{
	int a,b;
	b=1;
	for(a=1;a<=10;a+=1)
		b=b*a;
	printf("%d!은 %d로 계산됩니다.\n",a-1,b);
}