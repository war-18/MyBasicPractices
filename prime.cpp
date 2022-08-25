#include<bits/stdc++.h>
using namespace std;

void  Problem1(int time,int weight){
    if(weight ==0){
 cout<<"weight is 0 time is 0"<<endl;
    }
    else if(weight <2000 ){
        time=25;
    }
    else if (weight >2000 and weight <4000){
        time=45;
        cout<<"time is"<<time<<endl;
    }
    else {
        cout<<"Overload"<<endl;
    }
}




int reverseArr(int arr[],int n){
    int arr1[n];
    for(int i=n;i>=0;i++){
    
    }
    return 0;
}



bool prime(int n){
    for(int i=2;i<sqrt(n);i++){
        if(n%i==0){
            return 0;
        }
        else{
            return 1;
        }
    }
}



int GCD(int a,int b){
    if(a==b){
        return a;
    }
    if(a>b){
        return GCD(a-b,b);
    }
    else{
        return GCD(a,b-a);
    }
}

int fact(int n){
    if(n==0 || n==1){
        return 1;
    }
    else if (n<0){
        return -1;
    }
    else{
        return n*fact(n-1);
    }
}

int main(){
    
    int x;
    cin>>x;
//factorial
cout<<fact(x)<<endl;
//GCD
int a=60,b=30;
cout<<GCD(a,b)<<endl;

cout<<" isPrime "<< x;
cout<<prime(x)<<endl;



cout<<"***********Problem 2**********"<<endl;
int IntWall,ExtWall;
cin>>IntWall>>ExtWall;
int totalInput=IntWall+ExtWall;

int addIntSurfaceArea=0,addExtSurfaceArea=0;

while(totalInput--){
    int IntSurfaceArea,ExtSurfaceArea;

    for(int i=0;i<IntSurfaceArea;i++){
        cin>>IntSurfaceArea;
        addIntSurfaceArea+=IntSurfaceArea;
    }

    for(int i=0;i<IntSurfaceArea;i++){
        cin>>ExtSurfaceArea;
        addExtSurfaceArea+=IntSurfaceArea;
    }

    

}

cout<<"Painting Cost is"<< (addIntSurfaceArea*18)+(addExtSurfaceArea*12)<<endl;



cout<<"**********Problem3************"<<endl;

int n,k,j,m,p;

cin>>n,k,j,m,p;

int N1=0;
int N2=0;
if(k>0){
    int N1=m/k;
}
if(j>0){
    int N2=p/j;
}
int N3=n-N1-N2;
cout<<"Number of Monkey Left in tree"<<N3<<endl;

}