#include<stdio.h>
#include<time.h>
#include<math.h>
void my_swap(int *p,int f,int l)
{
	int temp=0;
	temp=*(p+f);
	*(p+f)=*(p+l);
	*(p+l)=temp;

}
void selection()
{
int n,i,j,min;
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


int l=sizeof(a)/sizeof(a[0] );

	printf("---------------------------\n");
t1=clock();
	for (i=0;i<l;i++)
	{
		int min =i;
		for(j=i+1;j<l;j++)
		{
			if(a[j]<a[min])
			{
				min=j;
			}
		}
		if(min!=i)
		{
			my_swap(a,i,min);

		}
	}

t2 = clock();
	printf("\n\nselection sort order:- ");
	for (i=0;i<l;i++)
	{
		printf("%d ",a[i]);
	}

//	printf("\n %.4ld\n",start);
//	printf("\n %.4ld\n",end);
printf("\ntime taken for selection sorting=%f \n",( (float)t2 - (float)t1) /CLOCKS_PER_SEC );
}
