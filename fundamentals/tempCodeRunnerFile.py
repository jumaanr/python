#--- Iterating List
ages = [34,25,56,99,45,81,22,76,37,34]
total = 0
for age in ages:
    total += age
average = total / len(ages)
print(average)