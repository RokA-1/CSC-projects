#Creating variables and taking their input values
name=input("What is your name? ")
age= input("What is your age? ")
no1,no2=map(int,input("Enter your most two favourit numbers: ").split())

#Makinng the ration between numbers
ratio= no1/no2

#Printing results
print("Hello",name)
print("Your age is",age)
print("The ratio of your favorite numbers is",ratio)