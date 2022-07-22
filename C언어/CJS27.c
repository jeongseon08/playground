//최정선#27-시간(초단위)를 입력받아 시간, 분 ,초 인지를 출력
#include<stdio.h>
void main()
{
int t,t1,h,m,s;//정수형변수선언
printf("몇초를 입력하실것입니까?");
scanf("%d",&t); //입력함수
t1=t;
h=t/3600;
t=t%3600;
m=t/60;
t=t%60;
s=t;
printf("입력한 시간%d초는 %d시간%d분%d초입니다.\n",t1,h,m,s);
}