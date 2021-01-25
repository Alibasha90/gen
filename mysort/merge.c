

void my_merge(int arr[],int i1,int j1,int i2,int j2);
void mergeSort(int arr[],int i,int j)
{
	int mid;

	if(i<j)
	{
		mid=(i+j)/2;
		mergeSort(arr,i,mid);		//left recursion
		mergeSort(arr,mid+1,j);	//right recursion
		my_merge(arr,i,mid,mid+1,j);	//merging of two sorted sub-arrays
	}
}

void my_merge(int arr[],int i1,int j1,int i2,int j2)
{
	int temp[50];	//array used for merging
	int i,j,k;
	i=i1;	//beginning of the first list
	j=i2;	//beginning of the second list
	k=0;

	while(i<=j1 && j<=j2)	//while elements in both lists
	{
		if(arr[i]<arr[j])
			temp[k++]=arr[i++];
		else
			temp[k++]=arr[j++];
	}

	while(i<=j1)	//copy remaining elements of the first list
		temp[k++]=arr[i++];

	while(j<=j2)	//copy remaining elements of the second list
		temp[k++]=arr[j++];

	//Transfer elements from temp[] back to a[]
	for(i=i1,j=0;i<=j2;i++,j++)
		arr[i]=temp[j];
}
