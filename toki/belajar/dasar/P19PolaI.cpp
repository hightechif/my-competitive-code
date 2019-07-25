#include <bits/stdc++.h>
using namespace std;

int main()
{
	int a,b;
	cin>>a>>b;
	for (int i=1; i<a; i++)
	{
		if (i%b==0) cout<<"* ";
		else cout<<i<<" ";
	}
	if (a%b==0) cout<<"*"<<"\n";
	else cout<<a<<"\n";
	return 0;
}
