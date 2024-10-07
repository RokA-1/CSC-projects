#include <iostream>
using namespace std;

int main() {

  //Creating variables
  string name;
  int age, n1, n2;

  //Giving them values from input
  //Name
  cout << "What is your name? ";
  cin >> name;
  //Age
  cout << "What is your age? ";
  cin >> age;
  //Favourite digits
  cout << "What are your favourit two digits? ";
  cin >> n1 >> n2;
  //Ratio
  int ratio = n1/n2;

  //Printing results
  cout << "Hello " << name;
  cout << "\nYour age is " << age;
  cout << "\nThe ratio of your favorite numbers is " << ratio;
  
}