#include<stdio.h>
#include"header.h"
#include<stdlib.h>


int main()
{
	int i,n;
	int arr[n];
	int mid;
	char ch[3];
	int low =0;
	int high=sizeof(arr)/sizeof(arr[0] )-1;
	while(1)
	{
		printf("\n\n1)insertion\n2)bubble\n3)select\n4)quick\n5)merge\n6)exit\n");
		printf("select sorting techniques:\n");
		scanf("%s",ch);

		//		ch=atoi(argv[1]);
		int var = atoi(ch);
		switch(var)
		{


			case 1:insert();break;

			case 2:bubble_sort();break;

			case 3:selection();break;

			case 4:
			       printf("enter no.of n=");
			       scanf("%d",&n);
	printf("please enter only signed int or unsigned int\n");
			       for(i=0;i<n; i++)
			       {
				       printf("enter the elements arr[%d]=",i);
				       scanf("%d",&arr[i]);
			       }
			       quickSort(arr,low,high);break;

			case 5:
			       printf("enter the no.of n=:");
			       scanf("%d",&n);
	printf("please enter only signed int or unsigned int\n");
			       for(i=0;i<n; i++)
			       {
				       printf("enter the elements arr[%d]=",i);
				       scanf("%d",&arr[i]);
			       }
			      

				mergeSort(arr,low ,high);break;

			case 6:exit(0);	        
		}
	}
}
