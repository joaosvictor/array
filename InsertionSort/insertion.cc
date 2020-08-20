// time complexity: O(n)
// https://en.wikipedia.org/wiki/Insertion_sort 

#include <bits/stdc++.h>
using namespace std; 
  
void insertionSort(int arr[], int n) { 
    int i, key, j;  
    for (i = 1; i < n; i++){ 
        key = arr[i];  
        j = i - 1;  
  
        while (j >= 0 && arr[j] > key){ 
            arr[j + 1] = arr[j];  
            j = j - 1;  
        }                             
        arr[j + 1] = key;  
    }  
}  
  
void printArray(int arr[], int n){
    int i;  
    for (i = 0; i < n; i++)  
        cout << arr[i] << " ";  
    cout << endl; 
}  
  
int main(){ 
    cout << "The sorted given list: " << endl;
    int arr[] = {90,7,85,13,71,22,67,36,59,45};  
    int n = sizeof(arr) / sizeof(arr[0]);  
  
    insertionSort(arr, n);  
    printArray(arr, n);  
  
    return 0;  
}  
  
