#include <bits/stdc++.h>
using namespace std;

int main()
{
	long long A,B,C,D,E,F,besar,kecil,hasil;
	cin>>A>>B>>C;
	besar = max(max(A,B),C);
	kecil = min(min(A,B),C);
	if ( (besar-kecil==2) && ( (A==besar && (A==B || A==C)) || (B==besar && B==C) ) )
	{
		hasil = 2;
		D = kecil;
		E = besar-3;
		F = E;
		hasil += min(min(D,E),F);
	}
	else
	{
		A-=kecil; B-=kecil; C-=kecil;
		hasil = kecil + A/3 + B/3 + C/3;
	}
	cout<<hasil<<"\n";
	return 0;
}
