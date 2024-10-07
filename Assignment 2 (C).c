#include <stdio.h>

int main(void) {
  // creating variables
  char Name[30];
  int Age;
  int first_no;
  int second_no;
  float ratio;
  
  // signing value for variables
  //name
  printf("What is your name? ");
  scanf("%s", Name);
  //age
  printf("How old are you? ");
  scanf("%d", &Age);
  //fav numbers
  printf("What are your favorite numbers? ");
  scanf("%d", &first_no, &second_no);
  //ratio
  ratio = first_no / second_no;

  //print results
  printf("Hello %s", Name);
  printf("Your age is %d", Age);
  printf("The ratio of your favorite numbers is %f", ratio);
  
  return 0;
}