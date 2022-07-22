#include <stdio.h>
void main()
{
int a,b,c;
c=0;
for(a=1;a<=9;a++)
{
printf("<%d단>\n",a);

for(b=1;b<10;b++) //곱해지는 수용 안쪽 for문
{
	c=a*b;
	printf("%dX%d=%2d\n",a,b,c);
}
printf("\n\n");
}
}