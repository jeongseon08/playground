#include <stdio.h>
void main()
{
int a,b,c;
b=0;
c=0;
a=1;
while(a<=100)
{
if(a%2==1)
	b=b+a;
else //¦���Ǵ�
	c+=a;
a=a+1;
	}
printf("Ȧ����=%d\n",b);
printf("�����=%d\n",c);
}
