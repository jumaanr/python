#Understanding Lists
List1 = [34,89,57,90,44,78]
List2 = List1
# another list created using the ...
print(List1[0])
print(List2[0])
#above prints the same values, however they are not two distinct lists. Because unlike variables the lists just holds the reference of values to the location of memory
"""
This is easily understood, when you change 1 element's value of List1 , since List2 also referencing to the same value , if you print the same element of List2,
it will print the same value

"""
List1[1] = 63
print(List2[1])  #This printed up the same value as List[1]
#Lets see if the memory references are same 
print(hex(id(List1[0]))) #printing memory address of the first item in the list1 : result 0x7ffb05a2cdd8
print(hex(id(List2[0]))) #printing memory address of the first item in the list2 : result 0x7ffb05a2cdd8

#To overcome this we can slice a list
"""
We can slice a list using list[start:end]
specifiying the start and end index on how we want to slice the list
Elements on the 'start' index should be the first element included in the new list
Elements of the 'end' index wont be included in the new slice list, but it will slice exactly before that element

"""
letters = ["A","B","C","D","E"]

slice_firsttwo = letters[0:2]
print(slice_firsttwo) #prints ['A','B']

slice_allthewaytoend = letters[1:]
print(slice_allthewaytoend) #prints ['B','C','D','E'] , useful when we dont know exact size of the list

slice_firstAndlastCutoff = letters[1:-1]
print(slice_firstAndlastCutoff) #prints ['B', 'C', 'D']

slice_exactCopy = letters[:]
print(slice_exactCopy) #prints ['A', 'B', 'C', 'D', 'E'] #This creates an identical  copy but its memory locations are different

# We can also use del keyword to manupilate lists, however this modifies the original list
letterz = ["A","B","C","D","E"]
del letterz[1:3]
print(letterz) #prints ['A', 'D', 'E'] , index 1=B to index 3-1=2 , C is removed

del letterz[:] #deletes all elements in the array
print(letterz) #prints []

#-----------Searching through a list --------------#
letters = ["A","B","C","D","E"]
print("B" in letters) # output : True , this search wherether B is in the list and gives a boolean result
print("Z" in letters) # output : False, this search whether Z is in the list and gives a boolean result

print("B" not in letters) # output : False , this searches where B is not in the list, gives the result in boolean form
print("Z" not in letters) # output : True , this searches where Z is not in the list, tives the results in boolean form

#------------- Nested Lists -----------------#
"""
This comprises of the lists consists of other list , aka 2D array
Lets say this is a class room where students are placed:

    0       1      2    3
0   [Sam | Max | Joe | Ann ]
1   [Pam | Leo | Guy | Tim ]
2   [Zoe | Eva | Liz | Kim ]

Lets see how this implemented in a 2D array

"""

classroom = [

    ["Sam","Max","Joe","Ann"],
    ["Pam","Leo","Guy","Tim"],
    ["Zoe","Eva","Liz","Kim"],

]

#Lets see how can we retrive Tim
student = classroom[1][3]
print(student) #Prints Tim