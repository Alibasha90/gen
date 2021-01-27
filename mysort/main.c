#include<stdio.h>
#include"header.h"
#include<stdlib.h>
#include<time.h>

int main()
{
	clock_t t1,t2;
	int n,i,high,j;
	int mid;
	int ch,var;

//	while(1)
//	{
		printf("\n\n1)insertion\n2)bubble\n3)select\n4)quick\n5)merge\n6)exit\n");

		printf("select sorting techniques:\n");
		scanf("%d",&ch);
		
		if(ch<4 | ch ==6)
		{

			switch(ch)
			{

				case 1:insert();break;
				case 2:bubble_sort();break;
				case 3:selection();break;
				case 6:exit(0);	        
			}
		}
		else
		{
	printf("enter no.of n=");
	scanf("%d",&n);
	int arr[n];
			switch(ch)
			{
				case 4:
					high=sizeof(arr)/sizeof(arr[0])-1;
					printf("enter only signedint or unsignedint\n");
					for(i=0;i<n; i++)
					{
						printf("enter the elements arr[%d]=",i);
						scanf("%d",&arr[i]);
				
		
	
					}
					t1=clock();
					quickSort(arr,0,high);
					t2=clock();
					printf("\n\nQuick sorted output:-");
					for(i=0;i<n;i++)
					{
						printf("%d ",arr[i]);
					}
					
					
					printf("\ntime taken for Quick sort ( %f ) milli seconds \n", ( (float)t2-(float)t1)/CLOCKS_PER_SEC);
					break;




				case 5:

					j=sizeof(arr)/sizeof(arr[0])-1;
					printf("enter only signedint or unsignedint\n");
					for(i=0;i<n; i++)
					{
						printf("enter the elements arr[%d]=",i);
						scanf("%d",&arr[i]);
					}

					t1=clock();
					mergeSort(arr,0,j);
					t2=clock();
					printf("\n\nMerge sorted output:-");
					for(i=0;i<n;i++)
					{
						printf("%d ",arr[i]);
					}
					printf("\ntime taken for Merge sorting ( %f ) milli seconds \n", ( (float)t2-(float)t1)/CLOCKS_PER_SEC);

					break;

			}
		}
//	}
}

