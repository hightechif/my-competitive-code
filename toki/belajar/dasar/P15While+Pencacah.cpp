#include <bits/stdc++.h>
using namespace std;

int main()
{
	int x,h=0;
	do
	{
		cin>>x;
		if(cin.eof()) break;
		h += x;
	} while(true);
	cout<<h<<"\n";
	return 0;
}
