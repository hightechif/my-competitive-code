/*
ID: ridhanf1
LANG: C++
TASK: test
*/
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	//KAMUS
	string NAME1 = "test.in";
	string NAME2 = "test.out";
	ifstream fin;
	ofstream fout;
	string s1;
	int i1;
	
	//ALGORITMA
	fin.open(NAME1);
	fin >> s1;
	fin >> i1;
	fout.open(NAME2);
	fout << s1;
	fout << i1;
	fin.close();
	fout.close();
	return 0;
}
