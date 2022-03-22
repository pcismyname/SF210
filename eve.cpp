#include<iostream>

using namespace std;

int const PRICE = 100;


void hello(){
    cout<<"This is buffet!!!"<<endl;
}

int inform(){
    int num;
    cout<<"Number of customer";cin>>num;
    return num;
}

double cost(int num){
    double cost1 = num * PRICE;
    return cost1;
}

void vat(double cost){
    cout<<"Total cost : "<<cost*1.07;
}


int main(){
   hello();
   int num = inform();
   double cost1 = cost(num);
   vat(cost1);
}

