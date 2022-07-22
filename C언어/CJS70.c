//최정선70*-반환값이 있거나 없는 함수연습
#include <stdio.h>
void abc(); //함수선언부, 리턴값이 없으므로 void 형으로
char xyz(); //함수선언부, 리턴값이 정수형이므로 int형으로 선언
void main() //리턴값이 없으므로 void 형으로선언
{
int a; //지역변수선언
abc();
a=xyz(); //함수호출, 리턴값을 변수a가 받음
printf("호출된 함수xyz()의 리턴값=%d\n",a);
}
void abc()  //함수 정의부
{
	printf("안녕하세요 abc()함수입니다.\n");
}
char xyz() //함수정의부, 리턴값이 정수이므로int형으로
{
return s; //호출된 곳에 값을 리턴(전달)문
}