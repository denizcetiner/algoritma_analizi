#include <iostream>

using namespace std;
int step_log=0;
int step_linear=0;

int power_function_log(int x,int n)
{
    step_log=step_log+1;
    if(n==0) return 1;
    else if (n==1){
        return x;
    }
    else if (n%2==0)
    {
        return power_function_log(x*x, int(n/2));
    }
    else
    {
        return power_function_log(x*x,int(n/2)) * x;
    }

}

int power_function_linear(int x,int n)
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
    cout << pow_log(2,16) << endl;
    cout << step_log<<endl;
    cout << power_function_linear(2,16)<< endl;
    cout << step_linear;
    return 0;
}

