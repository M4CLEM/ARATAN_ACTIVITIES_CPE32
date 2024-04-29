#1.Display numbers from -10 to -1 using for loop

for num in range(-10, 0):
    print(num)

#2. Use else block to display a message “Done” after successful execution of for loop

for nums in range(-10, 0):
    print(nums)
else:
    print("Done\n")

#3.Write a program to display all prime numbers within a range

Start, End = 0, 10

for number in range(Start, End + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number, "\n")

#4.Use a loop to display elements from a given list present at odd index positions

given_list = [1, 2, 3, 4, 5, 6]

for index in range(1, len(given_list), 2):
    print(given_list[index])

#5. Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)