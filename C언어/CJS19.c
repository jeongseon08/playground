//최정선19***-증가 연산자 연습
#include<stdio.h>
void main()
{
int a,b,c; //정수형변수선언
a=10;
b=0, c=0; //변수 초기화
printf("a=%d,b=%d,c=%d\n",a,b,c);
b=a++;
//후행(후치)증가연산자, a값을 b에 대입한 후 a 자신의 값을 1만큼 증가시킨다.
printf("a=%d,b=%d,c=%d\n",a,b,c);
a=10,b=0,c=0;
printf("a=%d,b=%d,c=%d\n",a,b,c);
b=++a;
//선행(전치) 증가연산자, a값을 1만큼 증가시킨다음에 b에 대입
printf("a=%d,b=%d,c=%d\n",a,b,c);
a=10,b=0,c=0;
b=a++;
c=++a;
printf("a=%d,b=%d,c=%d\n",a,b,c);
}