#include <stdio.h>

void main()
{
int a,b,c,d;
d=0;
for(a=2;a<=9;a++)
	printf("#Á¦%d´Ü#",a);

printf("\n\n");

for(b=1;b<=9;b++)
{
	for(c=2;c<=9;c++)
{
d=c*b;
printf("%2dX%d=%2d",c,b,d);
}
printf("\n");
}
}