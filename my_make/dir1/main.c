#include<stdio.h>
#include "sub.h"
#include "../dir2/add.h"

int main()
{
int a=10,b=20;
	printf("add a + b = %d\n",add(a,b));
	printf("sub a - b = %d\n",sub(a,b));
//	printf("mul a * b = %d\n",mul(a,b));
}
