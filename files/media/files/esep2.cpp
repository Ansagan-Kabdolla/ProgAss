# include <iostream>
#include <conio.h>
# include <cmath>
using namespace std;
int main(){
	float b,t,z,x,y;
	cout << "Vvedite B: " ;
	cin >> b;
	
	if (b>1) 
		t=b*b;
	else 
		t=exp(b);
		
	z = sqrt(abs(sin(abs(b))));
	x = (b*sqrt(z+1))/(t*z+1);
	y = b*log(sqrt(x+t)+sqrt(x))-sqrt(x*x+t*x);
	cout << "t = "<< t <<"\n";
	cout << "z = "<< z <<"\n";
	cout << "x = "<< x <<"\n";
	cout << "y = "<< y <<"\n";
	getch();
	return 0;
}

