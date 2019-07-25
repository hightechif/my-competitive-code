#include <iostream>
#include <list>
#include <cmath>
using namespace std;

int sieve(int n)
{
	list<int> x (n+1,1);
	
	for (int i=2; i<=int(pow(n,0.5)); i++)
	{
		if (x[i]==1)
		{
			for (int j=2; i*j<=n; j++) x[i*j] = 0;
		}
	}
	return x;
}

int main()
{
	int n,daftar[n+1];
	cin >> n;
	sieve(n);
	cout << daftar;
	return 0;
}
