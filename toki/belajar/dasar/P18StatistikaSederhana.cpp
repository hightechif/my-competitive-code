#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,temp,ma=-100000,mi=100000;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cin>>temp;
		ma = max(ma,temp);
		mi = min(mi,temp);
	}
	cout<<ma<<" "<<mi<<"\n";
	return 0;
}
