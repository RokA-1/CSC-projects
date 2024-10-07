using System;

class Program {
  public static void Main (string[] args) {
    Console.WriteLine ("Hello World");
  
    //Creating variables and assigning values with input
    //Name
    Console.WriteLine("What is your name? ");
    string name = Console.ReadLine();
    //Age
    Console.WriteLine("What is your age? ");
    int age = Convert.ToInt32(Console.ReadLine());
    //Fav numbers
    Console.Write("Write your first favorite number: ");
    int n1=Convert.ToInt32(Console.ReadLine());
    Console.Write("Write your second favorite number: ");
    int n2=Convert.ToInt32(Console.ReadLine());

    //Printing results
    Console.WriteLine("Hello, "+ name);
    Console.WriteLine("Your age is " + age);
    Console.WriteLine("The ratio of your favorite numbers is " + n1/n2);
    
  }
}