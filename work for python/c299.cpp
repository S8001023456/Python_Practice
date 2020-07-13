#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>

int main(){
  int number;
  vector <int> numberlist;
  bool comparator = true;
  int reg;

  cin>>number;
  for(int i = 0; i < number; i++){
    cin>>reg;
    numberlist.push_back(reg);
  }


  sort(numberlist.begin(), numberlist.end());
  for(int i = 0; i != number - 1; i++){
    if(numberlist[i] + 1 == numberlist[i+1])
      comparator = false;
  }
  if(comparator == true)
    cout<<numberlist[1]<<numberlist[numberlist.size() - 1]<<"yes"<<endl;
  else
    cout<<numberlist[1]<<numberlist[numberlist.size() - 1]<<"no"<<endl;
}
