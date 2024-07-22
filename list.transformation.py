# The aim of this assignment is to practice advanced list operations and transformations.

# You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Sort the grades in descending order and display the sorted list.

# Indecies 0   1   2   3   4   5   6   7   8   9
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# neg In   0  -9  -8  -7  -6  -5  -4  -3  -2  -1
print("sorting grades in descending order")
grades.sort()
print(grades)

print('='*50)

# Task 2: Calculate the average grade from the list above and display it (reminder: The average is calculated by dividing the sum of all grades by the length of the grades list). 

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort 
print("average grade is: ", sum(grades)/len(grades))