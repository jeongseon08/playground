#include <stdio.h>
void main()
{
int a,b,c;
c=0;
for(a=1;a<=9;a++)
{
printf("<%d��>\n",a);

for(b=1;b<10;b++) //�������� ���� ���� for��
{
	c=a*b;
	printf("%dX%d=%2d\n",a,b,c);
}
printf("\n\n");
}
}