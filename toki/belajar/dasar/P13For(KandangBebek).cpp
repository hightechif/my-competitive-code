#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,b,s=0;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cin>>b;
		s += b;
	}
	cout<<s<<"\n";
	return 0;
}
