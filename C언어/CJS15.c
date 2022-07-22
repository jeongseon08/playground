//최정선15*-산술연산자연습
#include <stdio.h>
	void main()
{
//INPUT(입력) 변수선언 및 변수 초기화
int a; //정수형변수선언
int b,c; //정수형변수선언 2개추가
a=17; //변수 초기화
b=4; 
//PROCESS(처리)
c=a+b; //산술 연산자 (+)
printf("%d+%d=%d\n", a,b,c);
c=a-b; //빼기연산자(-)
printf("%d-%d=%d\n",a,b,c);
c=a*b; //곱하기연산자(*)
printf("%d=%dX%d\n",c,a,b);
printf("%d/%d=%d\n",a,b,a/b);//나누기 연산자(/), 정수를 정수로 나누면 결과는 몫이다.
c=a%b; //나머지연산자(%), 나누기의 나머지
printf("%d%%%d=%d\n",a,b,c); //화면에 %를 출력하기위해서는 %%로 표현한다.
//a(=17)을 b(=4)로 나눈 몫은 4, 나머지는 1이다.
printf("%d/%%%d=%d,%d\n",a,b,a/b,a%b);
printf("a(=%d)을 b(=%d)로 나눈 몫은 %d이고, 나머지는 %d입니다.\n,",a,b,a/b,a%b);
	}