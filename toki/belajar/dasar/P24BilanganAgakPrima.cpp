#include <bits/stdc++.h>
using namespace std;

int AP(int x)
{
	int bts = pow(x,0.5)+1, count=3;
	for(int i=2; i<bts; i++)
	{
		if(x%i == 0)
		{
			count +=1;
			if(count>4) return false;
		}
	}
	return true;
}

int main()
{
	int n,x;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cin>>x;
		if(AP(x)) cout<<"YA\n";
		else cout<<"BUKAN\n";
	}
	return 0;
}
