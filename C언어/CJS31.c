//최정선 31-기본if문연습2(실행문장이 2개이상일 경우)
#include<stdio.h>
void main()
{
int a; //정수형변수선언
printf("당신의 점수는?");
scanf("%d",&a);
if(a>=60) //입력받은 점수가 60이상이라면
{
printf("%d는 합격입니다.\n",a);
printf("축하합니다.\n");
}
}