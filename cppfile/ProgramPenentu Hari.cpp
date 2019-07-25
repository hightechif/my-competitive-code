#include <bits/stdc++.h>
using namespace std;

int dow(int y,int m, int d){
	static int t[]={0,3,2,5,0,3,5,1,4,6,2,4};
	y -= m<3;
	return(y+y/4-y/100+y/400+t[m-1]+d)%7;
}

int main(){
	string hari[] = {"Minggu","Senin","Selasa","Rabu",
						"Kamis","Jumat","Sabtu"};
	int y,m,d;
	cout<<"Tahun Bulan Tanggal : ";
	cin>>y>>m>>d;
	cout<<hari[dow(y,m,d)]<<endl;
	return 0;
}
