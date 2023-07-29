# Arithmatic Operators

#Exponential Operator **
print(2 ** 3)
print(2. ** 3)
print(2 ** 3.)
print(2. ** 3)

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
print(6. / 4) #returns 1.5
print(6. // 4) #returns 1.0
print(6. / -4) #returns 1.5
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

#If the two operators have the same priority we calculate it from Left to right
#Sub expressions are always calculated first
print (2 * (2+3)) #returns 10

