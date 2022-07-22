//최정선32**-if~else문 사용예제
#include<stdio.h>
void main()
{
int a; //정수형변수선언
a=200; //변수초기화
if(a<100)//a값이100보다 작다면
printf("%d는 100보다 작습니다.\n",a);
else//조건이 거짓인 경우(a값이 100보다 크거나 같다면)
printf("%d는 100보다 크거나 같습니다.\n",a);

}