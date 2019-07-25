#include <bits/stdc++.h>
using namespace std;

int main()
{
	int len;
	string n;
	cin>>n;
	len = n.length();
	switch(len)
	{
		case 1:
			cout<<"satuan\n";
			break;
		case 2:
			cout<<"puluhan\n";
			break;
		case 3:
			cout<<"ratusan\n";
			break;
		case 4:
			cout<<"ribuan\n";
			break;
		case 5:
			cout<<"puluhribuan\n";
			break;
	}
	return 0;
}
