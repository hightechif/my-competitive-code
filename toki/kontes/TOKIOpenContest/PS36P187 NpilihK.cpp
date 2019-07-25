#include <bits/stdc++.h>
#define Titip using 
#define Absen namespace 
#define Dong std
Titip Absen Dong;

int main() {
	int n,k,x,j=1000000000;
	vector<int>data;
	cin>>n>>k;
	for(int i=0; i<n; i++){
		cin>>x;
		data.push_back(x);
	}
	sort(data.begin(),data.end());
	for(int i=0; i<n-k+1; i++){
		j = min(j,data[i+k-1]-data[i]);
	}
	cout<<j<<"\n";
	return 0;
}
