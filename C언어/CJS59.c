//최정선59-키보드로부터 입력받은 값을 배열에 저장
#include<stdio.h>
void main()
{
int a[3];
int b;
printf("첫번째 원소는?");
scanf("%d",&a[0]);
printf("두번째 원소는?");
scanf("%d",&a[1]);
printf("세번째 원소는?");
scanf("%d",&a[2]);
b=a[0]+a[1]+a[2];
printf("첫번째 원소는=%d\n",a[0]);
printf("누적합=%d\n",b);
}