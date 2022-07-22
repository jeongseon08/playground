//최정선9*-서식문자연습
#include <stdio.h>
void main()
{
printf("서식문자연습\n"); //\n 줄비꿈
printf("\n\n\n"); // 3줄 바꿈
printf("최\n정선\n");
printf("최\t정선\n"); //\t Tab키 역할, 우측이동
printf("abcd\b");  // \b 백스페이스, 좌로 한칸 이동하면서 문자지워줌
printf("\n\n");
printf("abcdef\r"); //\r 커서를 해당줄의 첫번째 칸으로 이동(좌로)
printf("123456\n"); 
printf("최정선의 성적은\"A\"학점\n");
printf("최정선\\\\성적\\\n"); // 역슬래시 (\)출력
printf("비프음\a"); //경고음(비프음) 출력=\a
}