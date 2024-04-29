import array

#1. Write a Python program to create an array of 3 integers and display the array items. Access individual elements through indexes.

num_arr = array.array('i', [1, 3, 5])

for item in num_arr:
    print(item)

print(num_arr[0])
print(num_arr[1])
print(num_arr[2])

#2. Write a Python program to append a new item to the end of the array.
app_arr = array.array('i', [1, 3, 5, 7, 9])

app_arr.append(11)

print("Original array:", app_arr[:-1])
print("Append 11 at the end of the array:")
print("New array:", app_arr)

#3. Write a Python program to reverse the order of the items in the array.

rev_arr = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("Original array:", rev_arr[:-1])

rev_arr.reverse()

print("Reverse the order of the items:")
print(rev_arr)

#4. Write a Python program to find out if a given array of integers contains any duplicate elements. Return true if any value appears at least twice in the array, and return false if every element is distinct.

def find_duplicates(arr):
    return len(arr) != len(set(arr))

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 3, 5]

print(find_duplicates(arr1))
print(find_duplicates(arr2))

#5.Write a Python program to find the first duplicate element in a given array of integers. Return -1 if there are no such elements.

def first_duplicate(arr):
    found = set()
    for num in arr:
        if num in found:
            return num
        found.add(num)
    return -1

dup_arr1 = [1, 2, 3, 4, 5]
dup_arr2 = [1, 2, 3, 4, 1]
dup_arr3 = [1, 2, 3, 4, 4, 2, 1]

print(first_duplicate(dup_arr1))
print(first_duplicate(dup_arr2))
print(first_duplicate(dup_arr3))