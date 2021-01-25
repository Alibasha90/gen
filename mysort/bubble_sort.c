#include<stdio.h>
#include<time.h>

void bubble_sort()
{
	int n;
	int temp=0,i,j,flag;
clock_t t1,t2;
	printf("enter no.of elements:");
	scanf("%d",&n);

	int arr[n];
printf("please enter only signed int or unsigned int\n");
	for(i=0;i<n; i++)
	{
		printf("enter the elements arr[%d]=",i);
		scanf("%d",(int *)&arr[i]);
	}

//-----------------------------------------------
t1=clock();

	for(i=0;i<n-1;i++)
	{
		flag=0;
		for(j=0;j<n-1-i;j++)
		{
			if(arr[j]>arr[j+1])
			{
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
				flag=1;
			}
		}
		if(flag==0)
			break;
	}
t2=clock();
printf("\n\nbubble sorted order:- ");
	for(i=0;i<n;i++)
	{
		printf("%d  ",(int)arr[i]);

	}
	printf("\ntime taken %f milli seconds \n", ( (float)t2-(float)t1 )/CLOCKS_PER_SEC);

	printf("\n\n");
}


