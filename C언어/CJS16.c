//최정선16*-관계연산자연습
#include<stdio.h>
void main()
{
int a,b,c; //정수형 변수 선언
a=100; //변수 초기화
b=200;
printf("%d==%d의 결과는 %d\n",a,b,a==b);
//2개항의 값이 같은지를 판단하는 관계연산자는 ==을 사용한다.
printf("%d!=%d\n",a,b,a!=b); //같지않은지를 판단하는 관계연산자는 !=을 사용한다.
printf("%d>%d:%d\n",a,b,c=a>b);
printf("%d<=%d:%d\n",a,b,c=a<b);//관계 연산자의 결과는 참 (1) 또는 거짓(0)
printf("%d=%d:%d\n",a,b,a=b);//'='대입 연산자는 우측의 값 또는 수식의 결과를 좌측의 변수에 대입한다 즉,a=(b=200) 대입연산자이다.
printf("(%d+%d)>(%dx%d)?%d\n",a,b,a,b,(a+b)>(a*b));
}