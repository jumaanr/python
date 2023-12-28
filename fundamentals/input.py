"""
Input Function - input()
this prompts the user to input some data from console
A program that doesnt use any input function is called as deaf program

Rule : Value of an input is always a string
If you are using the value of inputs for arthimatic and logic , consider type casting

Integers - int()
Floating point - float()



"""

# Example : Capturing input
favourite_color = input("What is your favourite color")
print ("Your favourite color is " + favourite_color)

#Example : Type casting
age = input("How old are you")
print(int(age)-10)

#Example : Type casting during input
age = int(input("How old are you ?"))
print(age - 10)