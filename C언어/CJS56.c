//������56-goto���� Ȱ���� �б�(�̵�)����
#include<stdio.h>
void main()
{
int a,b;
b=0;
for(a=1;a<=1000;a=a+1)
{
b+=a;
printf("a=%d,b=%d\n",a,b);
if(b>2000) //�������� 2000�� �Ѿ��?!
	goto yyy; //�б�(�̵�)�� ���̺��� ����	
}
printf("for�� ��������\n");
yyy: 
printf("���� a=%d, ������=%d\n",a,b);
}