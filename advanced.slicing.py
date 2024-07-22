# 2. Advanced Slicing Techniques
# Objective: The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
print("Extracting second week temperatures")
extract = temperatures[7:13]
print("extract: ", extract)
83, 85, 86, 87, 88, 89, 90,

print('='*50)

# Task 2: Extract all the temperatures above 100 (reminder: when slicing to the end of a list you don't need a stop index).

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print("Extracting temperatures above 100")
extract = temperatures[23:]
print("extract: ", extract)

print('='*50)

# Task 3: extract temperatures from the 5th to the 10th.

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

print("extracting temperatures from 5th to 10th")
extract = temperatures[4:11]
print("extract: ", extract)
