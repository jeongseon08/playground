//������ 69-���������� ���������� ������
#include <stdio.h>
void abc();//(2)�Լ������ ;�ʼ�
	int b=400; //������������
void main()
{
int a;
a=100;
abc(); //�Լ�ȣ���
printf("a=%d\n",a);
printf("��������b=%d\n",b);
}
void abc()//(3)�Լ����Ǻ�
{
int a;
a=200;
printf("abc�Լ��������� a=%d\n",a);
printf("��������b=%d(abc()�Լ�������)\n",b);
a=a+b;
printf("a=%d\n",a);
}