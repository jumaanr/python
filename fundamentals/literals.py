"""
In Python, literals are used to represent fixed values that are assigned to variables or used within code. They are the basic building blocks of data, and their value is self-evident from their appearance in the code. In other words, literals are constants representing data that can be directly used without further computation or evaluation.

( name, cname, print - These are not literals )

Python supports several types of literals, including:

Four major types and other types of literals

1. Numeric literals: These represent numeric values and can be integers, floating-point numbers, or complex numbers. Examples of numeric literals include `42` (integer), `3.14` (floating-point), and `2 + 3j` (complex).
    Integers :
        Octal numbers = represented by 0o123 = decimal value is  8^2x1+8^1x2+8^0x3 = 64+16+3 = 83
        Hexa Decimal numbers = represented by 0x123 = decimal value is 16^2x1+16^1x2+16^0x3 = 291

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