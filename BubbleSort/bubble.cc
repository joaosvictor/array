// Time complexity: O(n^2)
// https://en.wikipedia.org/wiki/Bubble_sort

#include<iostream>
using namespace std;
int main ()
{
   int i, j,temp,pass=0;
   int a[10] = {90,7,85,13,71,22,67,36,59,45};
for(i = 0; i<10; i++) {
   for(j = i+1; j<10; j++)
   {
      if(a[j] < a[i]) {
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
      }
   }
pass++;
}
cout <<"The sorted given list: \n";
for(i = 0; i<10; i++) {
   cout << a[i] << " "; 
}
return 0;
}    
