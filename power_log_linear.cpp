#include <iostream>

using namespace std;
int step_number_log=0;
int step_number_linear=0;

int pow_log(int x,int n)
{
    step_number_log=step_number_log+1;
    if(n==0) return 1;
    else if (n==1){
        return x;
    }
    else if (n%2==0)
    {
        return pow_log(x*x, int(n/2));
    }
    else
    {
        return pow_log(x*x,int(n/2)) * x;
    }

}

int pow_linear(int x,int n)
{
    int result=1;
    for(int i=0;i<n;i++)
    {
        step_number_linear = step_number_linear + 1;
        result = result * x;
    }
    return result;
}

int main()
{
    cout << pow_log(2,21) << endl;
    cout << step_number_log<<endl;
    cout << pow_linear(2,21)<< endl;
    cout << step_number_linear;
    return 0;
}

