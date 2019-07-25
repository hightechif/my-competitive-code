#include <bits/stdc++.h>
#include <string>
using namespace std;

int main()
{
	int count=1,idx;
	string kalimat,kalimatBaru,a;
	while(true)
	{
		kalimatBaru="";
		getline(cin,kalimat);
		if(cin.eof()) break;
		for(string::iterator i=kalimat.begin(); i!=kalimat.end(); ++i)
	{
		a = *i;
		if(a=="\"" and count%2!=0)
		{
			idx = kalimat.find(a);
			kalimatBaru += "``";
			count +=1;
		}
		else if(a=="\"" and count%2==0)
		{
			idx = kalimat.find(a);
			kalimatBaru +=	"''";		
			count +=1;	
		}
		else
		kalimatBaru += a;
	}
	cout<<kalimatBaru<<"\n";
	}
	return 0;
}
