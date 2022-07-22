#include <stdio.h>
void main()
{
int a,b,c,d,e,f,g;
int s[6]; //6개의 정수값으로 구성된 배열 s를 선언, 배열은 원소갯수는 n개이지만 이름 즉, 배열명은 1개이다.
s[0]=10;
s[1]=20;
s[2]=30;
s[3]=40;
s[4]=50;
s[5]=60;
a=1;
b=2;
c=3;
d=4;
e=5;
f=6;
g=a+b+c+d+e+f;
g=s[0]+s[1]+s[2]+s[3]+s[4]+s[5];
printf("배열s의 합=%d\n",g);
}