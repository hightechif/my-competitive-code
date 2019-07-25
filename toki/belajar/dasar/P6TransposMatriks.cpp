#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a[3][3], trans[3][3], i, j;
	for(i=0; i<3; i++)
	for(j=0; j<3; j++)
	{
		cin>>a[i][j];
		trans[j][i]=a[i][j];
	}
	for(i=0; i<3; i++)
	for(j=0; j<3; j++)
	{
		if((j+1)%3==0)
		cout<<trans[i][j]<<"\n";
		else
		cout<<trans[i][j]<<" ";
	}
	return 0;
}
