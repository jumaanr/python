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
print("Hello World")

""" 

Here the print() is a function, function is a part of code that used to cause and effect or evaluate a value
Several types of functions

1. Built in functions
2. Modules
3. Custom Functions

Arguments to the function must be passed between ()
We can pass arguments to the functions enclosed with parantheseis function1(arg1,arg2)

Function Execution:

Python checks fewthings before executing a function

1. Checks the function name
2. Checks arugments passed
3. Jumps into the function
4. Executes the function
5. Return to your code
6. Resumes execution

print()

- Built in function : can be used without importing it
- Allows us to print values to console
- we can invoke it with parantheses
- We can pass the value we want to print as arguments between parantheses
- the backslash \ tells python that the next charachter has a special meaning (e.g. \n)


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
#Keyword Arguments
print("Hello",end="") #you can pass whatver value you want to add at the end of the line (instead of newline charachter comes by default)
print("Future Programmer")
print("Hello","Future","Programmer",sep="-") #sperate strings by the specified charachter
print("Hello","Future","Programmer",sep="-",end="#")
print("Hello"+" Future") #Concatenate strings (Only we can concatenate same type of argumens : example string + string , numn + num)
print(2+3)

#---------------- Python Literals----------------#
"""
In Python, literals are used to represent fixed values that are assigned to variables or used within code. They are the basic building blocks of data, and their value is self-evident from their appearance in the code. In other words, literals are constants representing data that can be directly used without further computation or evaluation.

(220, "Hello", "Python", -89  - These are literals)
( name, cname, print - These are not literals )

Python supports several types of literals, including:

Four major types and other types of literals

1. Numeric literals: These represent numeric values and can be integers, floating-point numbers, or complex numbers. Examples of numeric literals include `42` (integer), `3.14` (floating-point), and `2 + 3j` (complex).
    Integers :
        Octal numbers = represented by 0o123 = decimal value is  8^2x1+8^1x2+8^0x3 = 64+16+3 = 83
        Hexa Decimal numbers = represented by 0x123 = decimal value is 16^2x1+16^1x2+16^0x3 = 291

    Floating point numbers:
        These are non empty decimal fractions
            45.50, 12.1 , -90.0, 89.394
            0.0000000000000000000001 = 1e-22 (Represent numbers in more economical form)

2. String literals: These represent sequences of characters and are enclosed in single quotes (`'...'`) or double quotes (`"..."`). Examples of string literals include `'Hello, Python!'` and `"I am a string."`.

3. Boolean literals: These represent the truth values `True` and `False` and are used in logical operations and comparisons.
    Used numberic represntation where 1 for true and 0 for false

4. None literal: Represented by the keyword `None`, it denotes the absence of a value and is commonly used in situations where there is no specific value to assign.

5. List literals: Represented by square brackets (`[]`), these are used to define lists containing multiple items. For example, `[1, 2, 3]` is a list literal.

6. Tuple literals: Represented by parentheses (`()`), these are used to define tuples containing multiple items. For example, `(1, 'hello', 3.14)` is a tuple literal.

7. Dictionary literals: Represented by curly braces (`{}`), these are used to define dictionaries, which consist of key-value pairs. For example, `{'name': 'John', 'age': 30}` is a dictionary literal.

8. Set literals: Represented by curly braces (`{}`), these are used to define sets containing unique elements. For example, `{1, 2, 3}` is a set literal.

Here are some examples of Python literals:

"""
print('Hello! "Python" is cool')#print "Python" in double quotes
print("Hello! 'Python' is cool")#print 'Python' in single quotes'
#Use escapate charachter to use quotes within a string, Lets python know it is just a quote
print("Hello! \"Python\" is cool ")
print(1_000_000) #This prints 1000000 (easy way to represent larger numbers)
print(type(1_000_000))#This prints the type of the argument, its an integer


# Numeric literals
num_integer = 42
num_negative_integer = -89
num_octal= 0o123
num_hexa = 0x123
num_float = 3.14
num_complex = 2 + 3j

# String literals
string_single_quotes = 'Hello, Python!'
string_double_quotes = "I am a string."
string_with_quotes = "Hello \"Python\" is cool"

# Boolean literals
is_true = True
is_false = False


# None literal
empty_value = None

# List literals
my_list = [1, 2, 3]

# Tuple literals
my_tuple = (1, 'hello', 3.14)

# Dictionary literals
my_dict = {'name': 'John', 'age': 30}

# Set literals
my_set = {1, 2, 3}


print(type(10))

#---------------------Operators------------------#

# Arithmatic Operators

print(6+4) #prints 10
print(6+4.0) #prints 10.0
print(6-4) #prints 2
print(6-4.0) #prints 2.0

#Exponential Operator **
print(2 ** 3)
print(2. ** 3)
print(2 ** 3.) #returns 8.0
print(2. ** 3.)

#Devision Operator - All returning values are floating point values
print(10/2)
print(10./2)
print(10/2.)
print(10./2.)

#Floor devision operator //  (This helps to devide integers not returning float values, if not specified)

print(10//2) #returns 5
print(10.//2)
print(10//2.)
print(10.//2.)

#Also rounds the value towards less integer value
print(6 // 4) # returns 1

print(6. / 4) #returns 1.5
print(6. // 4) #returns 1.0
print(6. / -4) #returns -1.5
print(6. // -4) #returns -2.0


#Modulous Operator % - Helps to calculate the remainder
print(4 %2 ) #returns 0
print(5 % 2) #returns 1

#Binary Operator expects two arguments :  leftargument - rightargument

#Unary Operator : -2  Specifies the value should be negative
print(-6 - 6) #returns -12
print(10 - -6) #returns 16

#Operator Priority in Order
"""
1. Unary : +  -
2. Exponential : **
3. * /  //  %
4. +  -

"""
#Example
print(10 - 6 ** 2 / 9 * 10 + 1) #returns -29.0

"""
no unary operators
First 6**2 = 36
then 36/9*10  (same priority , then we calculate from left hand side) = 4*10 = 40.0
finally what remaining is : 10 - 40.0 + 1 , from left to right  -30.0 + 1 = -29.0
-29.0
"""

#If the two operators have the same priority we calculate it from Left to right
#Sub expressions are always calculated first
print (2 * (2+3)) #returns 10

#----------------------Comments----------------------

#----------------------< Variables >-----------------#
#Examples of Variables
amount_of_apples = 5
cost_of_apples = 4
_total_cost =3
COST_OF_APPLE = 1
# Variable cannot be any of python's reserved words, if we are using it , start with uppercase

#Re assign values 
cost_of_apples = cost_of_apples + 2
cost_of_apples +=2

cost_of_apples = cost_of_apples - 2
cost_of_apples -=2

cost_of_apples = cost_of_apples * 2
cost_of_apples *=2

cost_of_apples = cost_of_apples ** 2
cost_of_apples **=2

cost_of_apples = cost_of_apples / 2
cost_of_apples /=2

cost_of_apples = cost_of_apples // 2
cost_of_apples //=2

cost_of_apples = cost_of_apples % 2
cost_of_apples %=2


#short way of doing the same
#shortcut operator works for all the operators

#----------------------User Inputs--------------------

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

#---------------------------------------------------------#
#------------------------< String Methods >---------------#
#---------------------------------------------------------#
#------------------------< Comparison Operators >---------------#

#from page 187 to 195

"""
There are 6 comparison operators

Equal       ==
Not Equal   !=
Greater than    >
Greater than or equal   >=
less than       <
less than or equal  <=

"""
print(2 == 2) #returns true
print(2 == 4) #returns false


#---------------------------------------------------------------#

