#Python program find difference between each number in the array and the average of all numbers

def find_difference_average(arr):
    differences = []
    average = sum(arr) / len(arr)

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]

        differences.append(diff)
    
    return differences, average

numbers = [10, 20, 30, 40, 50]
result = find_difference_average(numbers)
print(result)

#Python program to convert a string in an array

def string_to_array(arr):
    return list(arr)

in_string = "String"
print(string_to_array(in_string))

#Python program to split an array in two and store even numbers in one array and odd numbers in the other.

def split_even_odd(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]

    return even_numbers, odd_numbers

numbers_mix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_arr, odd_arr = split_even_odd(numbers_mix)
print("Even Numbers:", even_arr)
print("Odd Numbers:", odd_arr)

#Python program to perform insertion sort on an array.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers_to_sort = [52, 63, 22, 43, 50]
insertion_sort(numbers_to_sort)
print("Sorted Array:", numbers_to_sort)    