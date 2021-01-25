#include<stdio.h>
#include<time.h>

void insert()
{
	int i,j,temp,n;
clock_t t1,t2;
	printf("enter no.of elements:");
	scanf("%d",&n);

	int a[n];

printf("please enter only signed int or unsigned int\n");
	for(i=0;i<n; i++)
	{
		printf("enter the elements arr[%d]=",i);
		scanf("%d",&a[i]);
	}

int l=sizeof(a)/sizeof(a[0]);
	
t1=clock();
	for(i=1;i<l;i++)
	{
		temp=a[i];
		j=i-1;
		while(j>=0 && a[j]>temp)
		{
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=temp;
	}
t2=clock();

	printf("\n\ninsertion sort order:- ");

	for(i=0;i<l;i++)
	{
		printf("%d  ",a[i]);
	}
	printf("\n");
	printf("\ntime taken %f milli seconds \n", ( (float)t2-(float)t1 )/CLOCKS_PER_SEC);

}
