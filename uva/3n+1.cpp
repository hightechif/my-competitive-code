#include <bits/stdc++.h>
using namespace std;

int nilai(int x)
{
	int i=1;
	while(x!=1)
	{
		i+=1;
		if(x%2!=0) x = 3*x+1;
		else x = x/2;
	}
	return i;
}

int main()
{
	int a,b,k,l;
	while(true)
	{
		cin>>a>>b>>k;
		if(cin.eof()) break;
		for(int i=a; i<b+1; i++)
		{
			l = nilai(i);
			if(k>l) continue;
			else k=l;
		}
		cout<<a<<" "<<b<<" "<<k<<"\n";
	}
	return 0;
}
