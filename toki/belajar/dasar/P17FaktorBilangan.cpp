#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,a;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		a = n-i;
		if (n%a==0)	cout<<a<<"\n";
	}
	return 0;
}
