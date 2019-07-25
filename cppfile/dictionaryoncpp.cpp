#include <iostream>
#include <map>
using namespace std;

typedef map<pair<int, int>, int> Dict;
typedef Dict::const_iterator It;

int main()
{
   Dict d;

   d[make_pair(0, 0)] = 0;
   d[make_pair(1, 2)] = 1;
   d[make_pair(2, 1)] = 2;
   d[make_pair(2, 3)] = 3;
   d[make_pair(3, 2)] = 4;

   for (It it(d.begin()); it != d.end(); ++it)
   {
      int i(it->first.first);
      int j(it->first.second);
      cout <<it->second <<' '
                <<d[make_pair(j, i)] <<'\n';
   }
}
