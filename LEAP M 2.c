#include <stdio.h>
int Leap(int year);
int main()
{
int year,O;
printf("Enter Year-");
scanf("%d", &year);
O=Leap(year);
 if(O==1)
        printf("%d is a leap year", year);
    else if(O==2)
        printf("%d is not a leap year", year);
    return 0;
}

int Leap(int year)
{
if((year%4==0 && year%100!=0)||(year%400==0)) 
return 1;
else
return 2;
}