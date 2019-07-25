#include <bits/stdc++.h>
using namespace std;

int main()
{
	float n;
	cin>>n;
	if (n>1)
	{
		while (n>2)	n /= 2;
		if (int(n)%2 == 0) cout<<"ya\n";
		else cout<<"bukan\n";
	}
	else if (n==1)
	{
		cout<<"ya\n";
	} 
	return 0;
}
