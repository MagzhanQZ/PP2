#include <iostream>
using namespace std;

int main(){
    int n, k;
    cin >> n >> k;
    int **arr = new int*[n];
    for(int i=0; i<n;i++){
        arr[i] = new int[k];
    }

    for(int i=0; i<n;i++){
        for(int j=0;j<k;j++){
            cin >> arr[i][j];
        }
    }
    for(int i=0; i<n;i++){
        for(int j=0;j<k;j++){
            if(i==3){
                continue;
            }
            else cout << arr[i][j]<<" ";
        }
        cout << endl;
    }

    for(int i=0; i<n; i++){
        delete [] arr[i];
    }

    delete[] arr;
}