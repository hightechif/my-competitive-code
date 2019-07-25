#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main()
{
	int t,employ[3],i;
	cin>>t;
	for(i=0; i<t; i++)
	{
		cin>>employ[0]>>employ[1]>>employ[2];
		sort(employ, employ+3);
		cout<<"Case "<<i+1<<": "<<employ[1]<<"\n";
	}
	return 0;
}
