// time complexity: O(n). It occurs in the case when the input is already/almost sorted. 
// https://en.wikipedia.org/wiki/Insertion_sort

#include <iostream>
using namespace std;

void recursiveinsertion(int arr[], int n){
  if (n <= 1)
      return;

  recursiveinsertion(arr, n-1);

  int last = arr[n-1];
  int j = n-2;

  while (j >= 0 && arr[j] > last){
    arr[j+1] = arr[j];
    j--;
  }
  arr[j+1] = last;
}

void printarr(int arr[], int n){
   for (int i = 0; i < n; i++)
       cout << arr[i] << " ";
}

int main(){
    
  cout << "The sorted given list: " << endl;  
  int arr[] = {90,7,85,13,71,22,67,36,59,45};
  int n = sizeof(arr)/sizeof(arr[0]);

  recursiveinsertion(arr, n);
  printarr(arr, n);

  return 0;
}
