#include <stdio.h>
void main()
{
	int a,b;
b=0;
for(a=1;a<=100;a++)
{
	if((a%5==0)||(a%8==0))
		{
			b=b+a;
	printf("a=%d\n",a);
	} //if���� �߰�ȣ
	}
printf("5��8�� �����=%d\n",b);
}