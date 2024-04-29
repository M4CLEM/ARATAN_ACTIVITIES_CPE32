#1. Write a Python function to find the maximum of three numbers.
numbers = [5, 25, 20]

def find_maximum(numbers):
    return max(numbers)

result = find_maximum(numbers)
print("Maximum number is:", result)

#2. Write a Python function to sum all the numbers in a list.
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_numbers(numbers_list):
    return sum(numbers_list)

total_sum = sum_numbers(numbers_list)
print("The sum of all numbers in the list is:", total_sum)

#3. Write a Python program to reverse a string.
def reversed_string(input_str):
    return input_str[::-1]

original_string = "Clemence"
reversed_string = reversed_string(original_string)
print("Reversed string is:", reversed_string)

#4. Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_upper_lower(count_input):
    upper_case_count = sum(1 for char in count_input if char.isupper())
    lower_case_count = sum(1 for char in count_input if char.islower())
    return upper_case_count, lower_case_count

count_text = "Hello World"
upper, lower = count_upper_lower(count_text)
print("Number of upper case letters:", upper)
print("Number of lower case letters:", lower)

#5. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def distinct_elements(distinct_list):
    return list(set(distinct_list))

original_list = [1,1,2,2,4,3,5,4,5,6,6,7,7,8,8,9]
distinct_list = distinct_elements(original_list)
print("List of distinct elements:", distinct_list)