#include <iostream>
#include <map>
using namespace std;

typedef map<string, string> Dict;
typedef Dict::const_iterator It;

int main()
{
   Dict buku;
   int n,q;
   string nama,no,tampil;
   cin>>n>>q;
   for (int i=0; i<n; i++)
   {
   		cin>>nama>>no;
   		buku[nama] = no;
   }
   for (int i=0; i<q; i++)
   {
   		tampil="NIHIL";
   		cin>>nama;
   		for (It it(buku.begin()); it != buku.end(); ++it)
   		{
      		string i(it->first); 
      		if (nama == it->first) 
			{
				tampil = buku[nama];
				break;
			}
   		}
   		cout<<tampil<<"\n";
   }
   return 0;
}
