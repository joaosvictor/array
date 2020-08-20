// time complexity: O(n^2)
// https://en.wikipedia.org/wiki/Selection_sort
#include <iostream>
#include <vector>

using std::cout;
using std::endl;

template <typename T>
int find_smallest(const std::vector<T>& arr){
  T smallest = arr[0];
  // stores index of the smallest value 
  int smallest_index = 0;

  for (int i = 0; i < arr.size(); i++){
    if (arr[i] < smallest){
      smallest = arr[i];
      smallest_index = i;
    }
  }
   return smallest_index;
}
template <typename T>
std::vector<T> selection_sort(std::vector<T> arr){
  std::vector<T> sorted;

  while (!arr.empty()){
    // find smallest element and add it to sorted arr
    int smallest_index = find_smallest(arr);
    sorted.push_back(arr[smallest_index]);

    arr.erase(arr.begin() + smallest_index);

  }
    return sorted;
}
int main() {
    std::vector<int> arr = {90,7,85,13,71,22,67,36,59,45};
    std::vector<int> sorted = selection_sort(arr);

    cout << "The sorted given list:" << endl;
    for (int num : sorted){
      cout << num << " ";
    }
    cout << endl;
}
