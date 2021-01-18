#include<stdio.h>
#include<stdlib.h>


int main(int argc,char *argv[])
{
	int sum=0,i;
	for(i=1;i<argc;i++)
	{
	sum+=atoi(argv[i]);
	}
	printf("%d\n",sum);
	printf("hello\n");
	
printf(" i modified at remote side \n");
	

	printf("i modified in local repo\n");
}
