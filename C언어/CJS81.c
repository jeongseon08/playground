//최정선81-표준입출력함수 연습
#include <stdio.h>
void main()
{
char a; //문자형 변수선언, 문자 1개입력받는용
char b[20]; //문자열배열선언, 문자1개이상 입력받음
a= getchar(); //괄호속에 아무런 형식이 없습니다.
	putchar(a); //출력할 변수또는 문자를 매개변수로 사용합니다.
gets(b); //문자열을 형식없이 입력받을 때 사용
puts(b); //괄호속에 있는 변수 또는 문자열을 형식없이 출력할 때 사용
}