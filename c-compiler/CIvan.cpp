#include <bits/stdc++.h>
#define Titip using
#define Absen namespace
#define Dong std
Titip Absen Dong;

int main()
{
	int n;
	long long temp, hasil=0;
	cin>>n;
	for (int i=0; i<n; i++)
	{
		cin>>temp;
		hasil = max(hasil*temp,hasil+temp);
	}
	cout<<hasil<<"\n";
	return 0;
}
