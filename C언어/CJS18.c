//최정선18*-대입연산자와 증감연산자사용 예
#include<stdio.h>
void main()
{
int a,b; //정수형변수선언
a=10;
printf("%d+=%d:%d\n",10,5,a+=5);
//"+="연산자는 더하기 후 좌측변수에 대입
b=(a-=5);
printf("a-=5의 결과는 %d\n",b);
//변수는 프로그램실행중 계속해서 변경될수 있다.
a=10; //다시 초기화
b=(a*=5);
printf("b의 결과는 %d\n",b);
a=10;
b=a; //변수 b에 a의 초기값을 대입
printf("a(%d)/=5:%d\n",b,a/=5);
a=10;
b=a;
printf("a%%=5:%d\n",a%=5);
printf("최종a=%d,최종b=%d\n",a,b);
}