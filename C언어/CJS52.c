#include<stdio.h>
void main()
{
int a,b; //������ ��������
b=0;
a=1; //�ݺ��� ���� �ʱⰪ
while(a<=100) //���ǽ�
{
b=b+a;
a++;
} //while��
printf("����=%d\n",b);
printf("����=%d\n",a);
}