//최정선14-c언어의 데이터형의 크기계산
#include<stdio.h>
void main()
{
printf("정수형(int형)의 크기=%d\n",sizeof(int));
printf("실수형(float)=%d\n",sizeof(float));
printf("실수형(double)=%d\n",sizeof(double));
printf("문자형(char)=%d바이트\n",sizeof(char));
//sizeof()함수는 내장함수(기본적으로 제공하는함수)로서 해당 데이터형의 메모리할당크기를 바이트단위로 출력해준다.
}