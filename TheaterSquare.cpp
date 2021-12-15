    #include <iostream>
    #include <cmath>
    #include <iomanip>
     
    using namespace std;
     
     
     
    int main(){
          double x, y, z;
          cin >>x>>y>>z;
          cout<<setprecision(0)<<fixed<< endl;
          cout<< (double)(ceil(x/z)*ceil(y/z));
          return 0;
    }
