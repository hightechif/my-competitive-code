#include <stdio.h>
#include <conio.h>

int main(void)
{
	
	int age;
	printf("Enter your age");
	scanf("%d", &age);
	
	if(age==60)
	{
		printf("easy cougar!");
	}
	else if (age==40)
	{
		printf("mom?");
	}
	else if(age==21)
	{
		printf("call me");
	}
	else
	{
		printf("jailbait!");
	}
	getch();
	}
