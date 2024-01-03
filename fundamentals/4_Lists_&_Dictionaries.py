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

#--- Iterating List--- iterate through items in a list
ages = [34,25,56,99,45,81,22,76,37,34]
total = 0
for age in ages:
    total += age
average = total / len(ages)
print(average)

#Understanding Lists
