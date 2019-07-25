#include <bits/stdc++.h>
using namespace std;

int cek(int x)
{
	int b=5;
	if(x<=1) return false;
	else if (x<=3) return true;
	else if (x%2==0 || x%3==0) return false;
	while(pow(b,2) <= x)
	{
		if (x%b==0 || x%(b+2)==0)
		{
			return false;
		}
		b += 6;
	}
	return true;
}

int main()
{
	int n,p;
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cin>>p;
		if (cek(p)) cout<<"YA\n";
		else cout<<"BUKAN\n";
	}
	return 0;
}
