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
while(a<=100);//���ǽ� �ݵ�� ���� ;�� ���δ�.
printf("����=%d,����a=%d\n",b,a);
}