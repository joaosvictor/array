// Time complexity: O(n^2)
// https://en.wikipedia.org/wiki/Bubble_sort

#include <bits/stdc++.h>
using namespace std;

void recursive_bubble(int arr[], int n){
  if (n == 1)
      return;

  for (int i = 0; i < n-1; i++)
      if (arr[i] > arr[i+1])
          swap(arr[i], arr[i+1]);

  recursive_bubble(arr, n-1);
}

void printarr(int arr[], int n){
  for (int i = 0; i < n; i++)
      printf("%d ", arr[i]);
  printf("\n");
}

int main(){
  int arr[] = {90,7,85,13,71,22,67,36,59,45};
  int n = sizeof(arr) / sizeof(arr[0]);
  recursive_bubble(arr, n);
  printf("The Sorted given list: \n");
  printarr(arr, n);
  return 0;
}//
