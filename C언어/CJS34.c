//������* 34-��øif��(�����������α׷�)
#include<stdio.h>
void main()
{
int a; //��������������
printf("����� ������?");
scanf("%d",&a);
if(a>=90) //90�� �̻��̶��
printf("A����\n",a);
else
if(a>=80) //80~89�� ���
	printf("B����\n");
else
if(a>=70) //70~79
	printf("C����\n");
else
if(a>=60) //60~69�� ���
	printf("D����\n");
else //00~59�� ���
	printf("F����\n");
}