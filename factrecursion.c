#include<stdio.h>
int fact(int);
void main() {
    int n;
    printf("Enter value of n:"); //5
    scanf("%d",&n);
    
    printf("The fact is %d",fact(n));
    
    // int f=1;
    // for(int i=1;i<=n;i++)
    //     f*=i;
    // printf("The fact is %d",f);

}
int fact(n) {
    if(n==0 || n==1) 
        return 1;
    else 
        return n*fact(n-1);
}
/*
5!=5*4*3*2*1=120

fact(5)
return 5*fact(4)

fact(4)
return 4*fact(3)

fact(3)
return 3*fact(2)

fact(2)
return 2*1

fact(1)
return 1



//Example program for global scope
void fun1();			
void fun2();
int count;			
void main()
{
	count = 100;
	fun1();
}
void fun1()
{
	printf("Count is = %d\n",count);
	fun2();
}
void fun2()
{
	int count;
	for(count = 0;count < 5;count++)
		printf("*");
}






//Example program to include user defined header file
#include<stdio.h>
#include “MyFile.h”
void main()
{
	int a=10,b=20;
	printf(“\n The sum=%d”, sum(a,b));
}


MyFile.h
#include<stdio.h>
#define sum(x, y)  (x+y)


*/

