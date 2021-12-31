#include <stdio.h>
int Leap(int year);
int main()
{
int year;
printf("Enter Year-");
scanf("%d", &year);
 if(Leap(year))
        printf("%d is a leap year", year);
    else
        printf("%d is not a leap year", year);
    return 0;
}

int Leap(int year)
{
if((year%4==0 && year%100!=0)||(year%400==0)) 
return 1;
else
return 0;
}