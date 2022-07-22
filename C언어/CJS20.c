//최정선20***-감소연산자
#include<stdio.h>
void main()
{
int a,b,c; //정수형 변수선언
a=10; //변수 초기화
printf("a=%d\n", a);
a--;//감소연산자, a값을 1만큼 감소시킨다. a=a-1
printf("a=%d\n", a);
a=10;
b=a--; //후치(postfix)감소연산자, b에 a값을 대입한 후 a값을 1 만큼 감소시킨다.
printf("a=%d, b=%d\n",a,b);
a=10;
c=--a; //전치(prefix)감소연산자, c에 a값을 1만큼 감소시킨 값
printf("a=%d, c=%d\n",a,c);
}