#include<stdio.h>
void main()
{
int a,b,c;
c=0;
printf("����� ���Ͻǰ̴ϱ�?");
scanf("%d",&b);
for(a=1;a<=9;a++)
	{
		c=b*a;
printf("%dX%d=%d,\n",b,a,c);
}
}