#include <bits/stdc++.h>
#define Titip using
#define Absen namespace
#define Dong std
Titip Absen Dong;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int arr[]={6,2,4,8},N;
	cin>>N;
	if(N==0)
	{
		cout<<1<<"\n";
	}
	else
	{
		cout<<arr[N%4]<<"\n";
	}
	return 0;
}
