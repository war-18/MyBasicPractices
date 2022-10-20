// // // #include <iostream>
// // // using namespace std;

// // // int main()
// // // {

// // //     long long t;
// // //     cin >> t;
// // //     while (t--)
// // //     {
// // //         long long n;
// // //         long long s;
// // //         cin >> n >> s;
// // //         long long ans = s / (n * n);
// // //         if (ans >= 0)
// // //             cout << ans << endl;
// // //     }
// // // }

// // #include<bits/stdc++.h>
// // using namespace std;

// // int main(){

// //    long long t;
// //    cin>>t;
// //    while(t--){
// //        long long  n;
// //        long long arr[n];
// //        for(long long i=0;i<=n;i++){
// //            cin>>arr[i];
// //        }

// //    }

// //}

// #include <bits/stdc++.h>
// using namespace std;

// class A
// {
// public:
//     void func()
//     {
//         cout << "Inherited"<<endl;
//     }
// };

// class B : public A
// {
// };

// class C : public B
// {
// };

// int main()
// {

//     B b;
//     b.func();

//     C c;
//     c.func();
// }

#include <bits/stdc++.h>
using namespace std;

void mergeArr(int arr[], int s, int e)
{
    int mid = (s + e) / 2;
    int first[mid - s + 1];
    int second[e - mid];

    int k1 = s;
    for (int i = 0; i < (mid - s + 1); i++)
    {
        first[i] = arr[k1++];
    }

    int k2 = mid + 1;
    for (int j = 0; j < (e - mid); j++)
    {
        second[j] = arr[k2++];
    }

    int i1 = 0;
    int i2 = 0;
    k1 = s;

    while (i1 < mid - s + 1 && i2 < e - mid)
    {
        if (first[i1] < second[i2])
        {
            arr[k1] = first[i1];
            k1++;
            i1++;
        }
        else
        {
            arr[k1++] = second[i2++];
        }
    }

    while (i1 < mid - s + 1)
    {
        arr[k1++] = first[i1++];
    }
    while (i2 < e - mid)
    {
        arr[k1++] = second[i2++];
    }
}
void mergeSort(int arr[], int s, int e)
{
    int mid = (s + e) / 2;
    if (s >= e)
    {
        return;
    }

    mergeSort(arr, s, mid);
    mergeSort(arr, mid + 1, e);

    mergeArr(arr, s, e);
}

int main()
{

    int arr[5] = {1, 3, 4, 2, 5};
    int s = 0, e = 5;

    mergeSort(arr, s, e);

    for (int i = 0; i <e; i++)
    {
        cout << arr[i] << " ";
    }
}