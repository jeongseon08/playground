//최정선77-함수호출시 매개변수 전달(Call by value 값을 전달)
#include <stdio.h>
void abc(int,int); //(2)함수선언부, 매개변수의 데이터형은 int(정수)형이고, 리턴값이 없으므로 void 형으로 선언
void main()
{
int a,b; //정수형 변수선언
a=100; //변수 초기화
b=200;
printf("초기의 a=%d, b=%d\n", a,b);
abc(a,b); //함수호출부, 매개변수 2개를 가지고
printf("함수호출후 a=%d, b=%d\n", a,b);
}
void abc(int x, int y) //(3)함수정의부, main()함수로부터 전달될 매개변수 a.b에 대응되는 정수형변수 x,y를 선언해준다.
{
int tmp; //정수형 지역변수선언 (임의의 임시변수선언)
tmp =x;
x=y;
y=tmp; //2개의 수를 교환하는 방법
} 
//주소나 값전달이 되지않아  a와b가 교환되지않습니다. 따라서 78에서 개선하겠습니당.