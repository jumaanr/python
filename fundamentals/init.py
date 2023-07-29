#print something out
print("Hello World")

#Python Internals
"""
Python is an interpreted langauage. "Python interpreter" takes our human friendly python code and parses it line by line.
Then it creates a machine friendly code which your own computer can understand and execute

The current python 3.0 we use is called as "CPython" which is built out of C Programming lanugage
Other varients

Cython - Directly written to C limiting the execution time and make it efficient
Jython - Written in Java
RPython - mainly used by developers who develop python itself

Execute python code in shell:

$python3 myfile.py

"""
#Python basics

#-------------------Print function--------------------------------------------------------------------------
print("Hellow Furture Python Programer")

""" 

Here the print() is a function, function is a part of code that used to cause and effect or evaluate a value
Several types of functions

1. Built in functions
2. Modules
3. Custom Functions

Arguments to the function must be passed between () 

Python checks fewthings before executing a function

1. Checks the function name
2. Checks arugments passed
3. Jumps into the function
4. Executes the function
5. Return to your code
6. Resumes execution

Important !: There cannot be more that one instruction per a line in Python

"""

print("check this one")
print("check this two")
print("check this three")

#newline charachter
print("Hello \nFuture Programmer")
#multi arguments
print("Hellow","Future","Programmer")#python combines together and print them all in one line
#special arguments to the print function
#Usually the newline charachter \n automatically added to end of the print function. But here we can provide the parameter to change it
print("Hello",end="") #you can pass whatver value you want to add at the end of the line
print("Future Programmer")
print("Hello","Future","Programmer",sep="-") #sperate strings by the specified charachter
print("Hello","Future","Programmer",sep="-",end="#")
print("Hello"+" Future")

#-------------------Print function--------------------------------------------------------------------------
"""
Function is a part pf your code that's used to cause an effect or evaluate a value
Can come from :
- Python (Built in functions)
- Modules
- Your own code

Arguments - We can pass arguments to the functions enclosed with parantheseis function1(arg1,arg2)

Function Execution

Python:
1. Checks function name is legal
2. Checks arguments passed
3. Jumps into the function
4. Executes the function
5. Returns to your code
6. Resumes Execution

print()

- Built in function : can be used without importing it
- Allows us to print values to console
- we can invoke it with parantheses
- We can pass the value we want to print as arguments between parantheses
- the backslash \ tells python that the next charachter has a special meaning (e.g. \n)

"""

