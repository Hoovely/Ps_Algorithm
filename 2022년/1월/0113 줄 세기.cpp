#include <iostream>
#include <string>
using namespace std;

int main()
{
	int cnt = 0;
	string s;
	
	while (getline(cin, s))
	{
		cnt++;
	}

	cout << cnt;
}
