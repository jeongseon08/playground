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
else //Â¦¼öÆÇ´Ü
	c+=a;
a=a+1;
	}
printf("È¦¼öÇÕ=%d\n",b);
printf("Âï¼öÇÕ=%d\n",c);
}
