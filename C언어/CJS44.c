#include<stdio.h>
void main()
{
int a,b;
b=0;
for(a=1;a<=10;a=a+1)
{
b=a+a;
printf("%2d+%2d=%2d\n",a,a,b);
}
}