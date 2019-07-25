#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,q,x,y,a,h[n],hitung;
	cin>>n;
	for (int i=0; i<n; i++) 
	{
		cin>>a;
		h[i] = a;
	}
	cin>>q;
	for (int k = 0; k<q; k++)
	{
		hitung = 0;
		cin>>x>>y;
		for (int j=0; j<n; j++)
		{
			if (h[j]>x and  h[j]<=y)
			{
				hitung += 1;
			}
		}
		cout<<hitung<<"\n";
	}
	return 0;
}
