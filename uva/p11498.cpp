#include <bits/stdc++.h>
using namespace std;

int main()
{
	int k,n,m,x,y,i;
	while(true)
	{
		cin>>k;
		if(k==0) break;
		else
		{
			cin>>n>>m;
			for(i=0; i<k; i++)
			{
				cin>>x>>y;
				if(x==n or y==m) cout<<"divisa\n";
				else if(x>n and y>m) cout<<"NE\n";
				else if(x>n and y<m) cout<<"SE\n";
				else if(x<n and y<m) cout<<"SO\n";
				else cout<<"NO\n";
			}
			}	
	}
	return 0;
}
