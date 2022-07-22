//최정선56-goto문을 활용한 분기(이동)연습
#include<stdio.h>
void main()
{
int a,b;
b=0;
for(a=1;a<=1000;a=a+1)
{
b+=a;
printf("a=%d,b=%d\n",a,b);
if(b>2000) //누적합이 2000을 넘어서면?!
	goto yyy; //분기(이동)할 레이블을 지정	
}
printf("for문 다음문장\n");
yyy: 
printf("최종 a=%d, 누적합=%d\n",a,b);
}