#include <iostream>
using namespace std;

     float add(float a, float b){
     	return a+b;
	 }
	 float sub(float a, float b){
     	return a-b;
	 }
	 float Prod(float a, float b){
     	return a*b;
	 }
	 float div(float a, float b){
	 	if(b!=0){
	 		return a/b;
		 } else {
		 	return 0;
		 }
	}
     	

 int main() {
 
	float x,y;
	char op;
	cout<<"Enter ist number "<<endl;
	cin>>x;
	cout<<"Enter Operator (+, -, / * ): "<<endl;
	cin>>op;
	cout<<"Enter 2nd number "<<endl;
	cin>>y;
	
	switch(op){
		case '+' :
			cout<< "Result: "<<add(x,y);
			break;

	case '-' :
			cout<< "Result: "<<sub(x,y);
			break;
	
	case '*' :
			cout<< "Result: "<<Prod(x,y);
			break;
	
	case '/' :
			cout<< "Result: "<<div(x,y);
			break;
	
	default : 
	cout<<"Invalid Operator";
	}


return 0;
}

