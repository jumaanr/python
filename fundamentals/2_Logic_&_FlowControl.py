#------------Conditionals-------------#

#if condition
"""
-------------------------------------
if condition True :
    print("The condition is True")
elif condition True:
    print("Only the secodn condition is True)
else:
    print("The condition is false)
--------------------------------------

- correct indendation is required

Nested implementation:

if condition1 True:
    if confition2 True:
        print("condition 1 & condition 2 is true)
    else:
        print("condition 1 is only true)
else:
    print("condition 1 & condition 2 is false)


"""
#Example code

myage = int(input("Please enter your age : "))
if myage > 25:
    print ("You are older than 25 years")
elif myage == 25:
    print ("You are 25 years old")
else:
    print("You are younger than 25 years")


if (5,10):
    print ("Hello")
#This will print true, In Python non-empty tuples considered as True
#conditions can be declared using parenthesis () or without parenthesis

#------------- Loops----------------------------

#----------- while loop---------- : while loop allows you to run a certain block of code as long as a certain condition is True

"""

while condition True:
    print("Runs until condition is True)
else:
    print("while also allows else statement)


you can also use break keyword to break an infinite loop

"""
#Example: Guessing Game
secret_number= 3
guess = int(input("Guess a number: "))
while (guess != secret_number):
    print("Your guess is incorrect")
    guess = int(input("Guess a number again: "))
else:
    print("Congratulations your guess was correct !")

#Example : Breaking loop
value = 2
while True:
    if value%3 == 0:
        break
    print(value)
    value +=2
#This loop breaks when the value equals 6
    
#--------for loop---------------: repeatedly run code block based on certain values , mostly n number of times (n is finite integer)
"""
#This range function generate values from 0 to 9 , 10 times running the loop [0,1,2,3,4,5,6,7,8,9]
# Then there is 'i' which is the control variable of the loop

for i in range(10):
    print(my code block is here)

for i in range(2,5):
    print(my code block runs only 3 times, where 2,3,4)

# You can also break the loop if certain conditions met

for i in range(5):
    if (i==2):
        break
    print("i is ", i)

#skip the execution of the code block underneath on a certain value

for i in range(5):
    if (i==2):
        continue
    print("i is: ",i)

#so here 'i is 2' wont be printed, instead python will go to the next value

"""
for i in range(10)
print(i)


#Here we can only use an integer with range() function
x = 'abcd'
for i in range(len(x)):
    print(i)
#We can also iterate through certain charachters of a string, this prints a,b,c,d (all in new lines)
x = 'abcd'
for i in x:
    print(i)
#converts to uppercase
x = 'abcd'
for i in x:
    print(i.upper())

#following go through each letter in KodeKloud
for letter in 'KodeKloud'
    print (letter)

#---------- Logical Operators--------------#

#  and use for logical AND gate, or use for logical OR gate, not used for logical NOR gate


#Example : Following logic finds if the two marriage partners are adults
bride_age = int(input("Please enter bridges age : "))
groom_age = int(input("Please enter groom's age : "))

if (bride_age >= 18 and groom_age >=18) :
    print("Congratulations! you can marry")
elif(bride_age >=18 or groom_age >=18 ):
    print("at least one of you are old enough to marry")
else:
    print("You are both chrildern, bring your parents")


#-----------Bitwise Operators--------------#

"""
Allows you to manupilate single bits of data
https://kodekloud.com/topic/bitwise-operators/

&  - bitwise AND
|  - bitwie OR
^  - bitwise XOR
~  - negation ( 1 for every 0 and 0 for every 1)

There are also shortcut operations

bti1 = bit1 & 22 ----> bit1 &= 22  (likewise)
bit |= 22
bit ^= 22

Bitshifting

Bit shift right >>
<< Bit shift left

print(22>>1)  : Move all the bits right by 1 position, 0 fills the most left bit " Results 11 , which is exactly the half
print(22<<1)  : Move all the bits left by 1 position, 0 fills the most right bit " Result is 44 , which exactly the double the size

Samewhise shifting by 2, its the integer devision by 4
You cannot use bitwise operations for floating point numbers

"""
#----------------------------------------------------
