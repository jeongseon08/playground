//최정선60***-배열원소의 합 계산(for문)
#include <stdio.h>
void main()
{
int a[4]; //정수형 배열선언, 4개의 원소로 구성
int b; //정수형 변수 선언, 1개의 원소
int c; //정수형변수선언
for(b =0; b<4; b++) //배열의 첫번째 원소는 첨자가 0부터 시작해서 n-1까지
{
	printf("%d번째 정수를 입력하세요: ",b+1);
scanf("%d",&a[b]);
}
c= a[0]+a[1]+a[2]+a[3]; //배열원소의 누적합
printf("배열원소의 합= %d\n",c);
c=0;
for(b=0;b<=3;b=b+1)
{
	printf("%d번째 배열원소?" ,b+1);
scanf("%d",&a[b]);
c=c+a[b];
}
printf("배열합= %d\n",c);
}