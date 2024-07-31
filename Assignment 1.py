# Code Snippet 1: Variable Name Typo

number_of_apples = 5
# print(number_of_apple)
print(number_of_apples)
# the name of the variable should be same


# Code Snippet 2: Accessing List Elements Out of Range

fruits = ["apple", "banana", "cherry"]
# print(fruits[3])
print(fruits[2]) 
# this will be correct index to print "cherry"
# index of a list start from 0 so: apple will be 0; banana will be 1; cherry will be 2;


# Debugging Exercise 3: Function Not Behaving as Expected

# def find_average(numbers):
#     sum = 0
#     for number in numbers:
#         # sum += number
#     average = sum / len(numbers)
#     return average
def find_average(numbers):
    sum = 0
    for number in numbers:
        sum += int(number) 
        # this will take every number as an integer
    average = sum / len(numbers)
    return average
    
numbers = [1, 2, 3, 4, 5, "6"]
average = find_average(numbers)
print(f"The average is: {average}")


# Exercise 4: Incorrect Dictionary Usage

# def update_record(records, name, score):
#   if name in records:
#       records[name].append(score)
#   else:
#       records[name] = score
def update_record(records, name, score):
    if name in records:
        records[name].append(score)
    else:
        records[name] = []  
        records[name].append(score)
 # Earlier the code stores the score with the name but not as list
 # Corrected code will create an empty list for the new student
 # then append the score in it
        
student_records = {"Alice": [88, 92], "Bob": [70, 85]}
update_record(student_records, "Charlie", 91)
update_record(student_records, "Alice", 95)
print(student_records)