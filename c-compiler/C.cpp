#include <bits/stdc++.h>
#define Titip using
#define Absen namespace
#define Dong std
Titip Absen Dong;

int main()
{
	int n;
	long long temp, hasil;
	cin>>n;
	if (n>=1) cin>>hasil;
	for (int i=1; i<n; i++)
	{
		cin>>temp;
		if (temp == 0 || hasil == 0) continue;
		else if (temp == 1 || hasil == 1)
		{
			hasil += temp;
			cout<<hasil<<endl;
		}
		else
		{
			hasil *= temp;
			cout<<hasil<<endl;
		}
	}
	cout<<hasil<<"\n";
	return 0;
}
