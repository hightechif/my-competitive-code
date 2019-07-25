#include <bits/stdc++.h>
#define Titip using
#define Absen namespace
#define Dong std
Titip Absen Dong;

int main()
{
	int idx;
	string x;
	string operasi[] = {"+","*","/","-"};
	cin>>x;
	for (int i=0; i<4; i++)
	for (int j=0; j<x.size(); j++)
	{
		if (operasi[i] == x[j])
		{
			a = i;
			idx = j;
		}
	}
	if (a == 0) cout<<(int(x[:idx]) + int(x[idx+1:]))<<"\n";
	else if (a == 1) cout<<(int(x[:idx]) * int(x[idx+1:]))<<"\n";
	else if (a == 2) cout<<(int(x[:idx]) / int(x[idx+1:]))<<"\n";
	else if (a == 3) cout<<(int(x[:idx]) - int(x[idx+1:]))<<"\n";
	return 0;
}
