#include <iostream>

using namespace std;
void print_array(int* arr, int length)
{
    int max_left=0;
    int temp_left=0;

    int max_right=0;
    int temp_right=0;
    cout<<"Sol taraf"<<endl;
    for(int i = length/2; i>0; i--)
    {
        temp_left = temp_left + arr[i-1];
        if(temp_left > max_left)
        {
            max_left = temp_left;
        }


        cout<<arr[i-1] <<endl;


    }
    cout<<"Sol max:"<<endl;
    cout<<max_left<<endl;
    cout<<"Sag taraf"<<endl;
    for(int i = length/2; i < length; i++)
    {
        temp_right = temp_right + arr[i];
        if(temp_right > max_right)
        {
            max_right = temp_right;
        }
        cout<<arr[i]<<endl;

    }
    cout<<"Sag max"<<endl;
    cout<<max_right<<endl;
    cout<<max_right+max_left<<endl;
    return;
}

int main()
{
    int asdf[8] = {4,-3,2,1,6,-1,-2,4};
    print_array(asdf,sizeof(asdf)/sizeof(int));


    return 0;
}

