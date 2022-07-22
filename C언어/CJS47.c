#include<stdio.h>
void main()
{
int a,b,c;
c=0;
printf("몇단을 구하실겁니까?");
scanf("%d",&b);
for(a=1;a<=9;a++)
	{
		c=b*a;
printf("%dX%d=%d,\n",b,a,c);
}
}