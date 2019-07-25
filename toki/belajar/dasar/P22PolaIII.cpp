#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,value=0;
	cin>>n;
	for(int i=1; i<=n; i++)
	{
		for(int j=0; j<i; j++)
		{
			cout<<value;
			value +=1 ;
			if(value==10) value=0;
		}
		cout<<"\n";
	}
	return 0;
}
