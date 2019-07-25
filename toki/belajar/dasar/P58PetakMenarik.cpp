#include <bits/stdc++.h>
using namespace std;

int n,m,h[110][110];

int gv(int x, int y)
{
	if (x == -1 or x == n or y == -1 or y == m)
	return 1;
	return h[x][y];
}

int main()
{
	int k,i,j;
	pair <int,int> o (0,0);
	pair <int,int> p (0,0);
	cin>>n>>m>>k;
	for (i=0; i<n; i++)
	for (j=0; j<m; j++)
	{
		cin>>h[i][j];
	}
	for (j=0; j<m; j++)
	{
		if(o != p) break;
		for (i=0; i<n; i++)
		{
			if (k == gv(i-1,j)*gv(i+1,j)*gv(i,j-1)*gv(i,j+1))
			{
				o = make_pair(i+1,j+1);
				break;
			}
		}
	}
	cout<<o.first<<" "<<o.second<<"\n";
	return 0;
}
