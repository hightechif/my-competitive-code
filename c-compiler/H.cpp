#include <bits/stdc++.h>
using namespace std;

int main()
{
	long u,b;
	string o;
	cin>>u>>b;
	if (b==0) o="YA";
	else if (u>=pow(2,b)) o="YA";
	else o="TIDAK";
	cout<<o<<"\n";
	return 0;
}
