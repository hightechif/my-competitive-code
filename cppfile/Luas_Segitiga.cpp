#include <iostream>
#include <cmath>
using namespace std;

int main (){
	float x,y,z;
	cin >> x >> y >> z;
	float s = (x+y+z)/2;
	float L = sqrt(s*(s-x)*(s-y)*(s-z));
	cout << L;
	return 0;
}
