#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	cin>>n;
	for(int i=1; i<=n; i++)
	{
		if (i==42)
		{
			cout<<"ERROR\n";
			break;
		}
		else if (i % 10 != 0) cout<<i<<"\n";
		else continue;
	}
	return 0;
}
