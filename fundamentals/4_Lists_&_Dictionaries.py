#----------- Lists-----------------#
"""
Index starts from 0 , which is the first item in the list
all the items are indexed


"""

countries = ["USA","UK","INDIA"]  #Declaring a list
countries[0] = "UK"  #Assigning values to an item in list
len(countries) #returns the length of the list
del countries[1]  #delete the value of item indexed 1
print(countries[-1]) #returns the last item in the list , negative elements read from the last item

#We can never access the item with index that is dont exist : "Getting Error : Index Out of Range"


#Change Data in List using Built in Python Methods
"""
Methods behave like a function and look like it, but its purpose is different
Where a function works on its own, but Methods owned by the data that it works for

Functions:

print()
input()

Methods:

list.append()
list.insert()

list.sort() - sorts the list ascending order (by default), Alpha numberic , please be aware this method modifies the array
list.reverse() - reverse the elements in the list

"""
countries.append("SPAIN") #value to end of the list
countries.insert(2,"ITALY") # insert data to specific index (insert a new item between values). 2 is the index it should have

#Swaping values in a list
temp = countries[0]
countries[0] = countries[1]
countries[1] = temp
# Easier method
countries[0], countries[1] = countries[1], countries[0]

list = [113,56,99,178]
list.sort()
print(list)
list.reverse()
print(list)

#--- Iterating through List--- iterate through items in a list

ages = [34,25,56,99,45,81,22,76,37,34]
total = 0
for age in ages:
    total += age
average = total / len(ages)
print(average)

#----------------Understanding Lists---------------------

List1 = [34,89,57,90,44,78]
List2 = List1
# another list created using the same 
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
#-------------Slicing Lists------------------------------
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

#-------------------------Searching through a list -------------------------------------------#
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
