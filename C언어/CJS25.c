//최정선25-섭씨온도를 입력받아 화씨온도로 변환
#include<stdio.h>
void main()
{
float c,f; //실수형 변수선언, 섭씨와 화씨
printf("변환하고자 하는 섭씨온도는?");
scanf("%f",&c); //표준입력함수
f=(c*1.8)+32; //섭씨온도를 화씨온도로 변환식,process
printf("섭씨%4.1f도는 화씨로 %4.1f입니다.\n",c,f); //Output
}