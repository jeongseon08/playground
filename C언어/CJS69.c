//최정선 69-지역변수와 전역변수의 차이점
#include <stdio.h>
void abc();//(2)함수선언부 ;필수
	int b=400; //전역변수선언
void main()
{
int a;
a=100;
abc(); //함수호출부
printf("a=%d\n",a);
printf("전역변수b=%d\n",b);
}
void abc()//(3)함수정의부
{
int a;
a=200;
printf("abc함수내에서의 a=%d\n",a);
printf("전역변수b=%d(abc()함수내에서)\n",b);
a=a+b;
printf("a=%d\n",a);
}