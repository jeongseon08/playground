//최정선24-2개의실수를 입력받아 연산처리
#include<stdio.h>
void main()
{
float a,b; //실수형변수선언
double c; //좀더 큰 범위의 실수는 double형으로 선언
printf("첫번째 수:");
scanf("%f", &a);
//입력함수는 키보드로부터 값을 입력 받아 변수선언할 때 할당받은 메모리의 영역을 나타내는 주소(번지)를 변수명 앞에 반드시 붙여줘야 한다.
printf("두번째수:");
scanf("%f",&b); //scanf("a영역",b영역)에서 a영역에는 %d또는 %f만 사용하고, \n또는 빈칸 등은 입력해서는 안된다.
printf("a=%f\n b=%f\n", a,b);
c=a+b;
printf("%f+%f=%5.2f\n",a,b,c);
printf("%fX%f=%f\n",a,b,a*b);
printf("%5.2f/%5.2f=%5.2f\n",a,b,a/b);
c=(int)a % (int)b;
//캐스트(cast)연산자, 변수의 데이터형을 강제변환시키려면 변수명 앞에 변환하고자 하는 데이터형을 괄호로 묶어서 붙여준다.
printf("%4.2f %% %4.2f=%4.2f\n",a,b,c);
}