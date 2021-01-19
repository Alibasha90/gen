#include<stdio.h>
void bubble_sort()
{
	int n;
	int temp=0,i,j,flag;

	printf("enter no.of elements:");
	scanf("%d",&n);

	int arr[n];
printf("please enter only signed int or unsigned int\n");
	for(i=0;i<n; i++)
	{
		printf("enter the elements arr[%d]=",i);
		scanf("%d",&arr[i]);
	}

//-----------------------------------------------
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

printf("\nbubble sorted order:\n");
	for(i=0;i<n;i++)
	{
		printf("%d  ",arr[i]);
	}
	printf("\n\n");
}


