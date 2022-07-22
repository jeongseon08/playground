//최정선68*-매개변수(파라미터)가 2개인 사용자정의 함수 #4
#include <stdio.h>
int abc(int, int); //매개변수가 정수형 2개인 함수선언부로서 리턴값이 정수형이므로 int형으로 선언한다.
void main()
{
int a;
a=abc(100,200); //매개변수가 2개인 함수 호출부, 리턴값 존재
printf("리턴값a=%d\n",a);
} //main()함수 정의부의 중괄호
int abc(int x, int y) //main()함수에서 호출될 떄 2개의 매개변수인 100, 200을 받기위한 매개변수 x와 y를 동일한 정수형 (int)으로 사용한다.
{
int r; //함수 abc()의 지역변수
r=x+y;
return r; //abc()함수의리턴값(ss)을 지정한다.
}