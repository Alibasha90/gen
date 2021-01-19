#include<stdio.h>
#include<stdlib.h>



void merging(int a[],int low, int mid, int high) {
	int l1, l2, i;
	int b[10]={};
	for(l1 = low, l2 = mid + 1, i = low; l1 <= mid && l2 <= high; i++) {
		if(a[l1] <= a[l2])
			b[i] = a[l1++];
		else
			b[i] = a[l2++];
	}

	while(l1 <= mid)    
		b[i++] = a[l1++];

	while(l2 <= high)   
		b[i++] = a[l2++];

	for(i = low; i <= high; i++)
		a[i] = b[i];

}

void mergeSort(int a[],int low,int high) 
{int mid,i;

	if(low < high) {
		mid = (low + high) / 2;
		mergeSort(a,low, mid);
		mergeSort(a,mid+1, high);
		merging(a,low, mid, high);
	}

	printf("\n merge sorted order :\n");   
	for (i=0;i<high;i++)
	{
		printf("%d ",a[i]);
	}
	printf("\n");
}


