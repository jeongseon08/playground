//최정선 29-마일을 입력받아 킬로미터로 계산
#include<stdio.h>
void main()
{	
int m;
int k;//마일을 킬로미터로 변환한 결과를 저장할 변수
printf("몇마일을 입력하실 겁니까?:");
scanf("%d",&m);
k=m*1.6; //1마일=1.6킬로미터
printf("%d 마일은 %dKm/h 입니다.\n",m,k);
}