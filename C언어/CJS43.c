//������43-1~100 Ȧ���� ¦������ ��� if�� ���
#include<stdio.h>
void main()
{
int a,b,c;
b=c=0;
for(a=1;a<=100;a++)
{
if(a%2==1)
	b=b+a;
else
	c=c+a;
}
printf("1���� 100������ Ȧ�� ��=%d\n",b);
printf("1���� 100������ ¦�� ��=%d\n",c);
}