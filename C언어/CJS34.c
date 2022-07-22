//최정선* 34-중첩if문(학점관리프로그램)
#include<stdio.h>
void main()
{
int a; //정수형변수선언
printf("당신의 점수는?");
scanf("%d",&a);
if(a>=90) //90점 이상이라면
printf("A학점\n",a);
else
if(a>=80) //80~89인 경우
	printf("B학점\n");
else
if(a>=70) //70~79
	printf("C학점\n");
else
if(a>=60) //60~69인 경우
	printf("D학점\n");
else //00~59인 경우
	printf("F학점\n");
}