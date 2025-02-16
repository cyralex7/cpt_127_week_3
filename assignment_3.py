
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.


# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.
def sum_all(num):

    total_sum = sum(num)
    print(f"the sum is: {total_sum}")

num = [2, 4, 6, 8, 10]

sum_all(num)

# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.

def avg_all(numbers):
    total = sum(numbers)
    avg = total / len(numbers)

    print(f"The average is: {avg}")

numbers = [5, 10, 15]
avg_all(numbers)

# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

def calculations(number_list):

    #calc
    totalsum = sum(number_list)
    avg = totalsum / len(number_list)
    largest = max(number_list)

    #print
    print(f"Sum: {totalsum}")
    print(f"Average: {avg}")
    print(f"Largest Number: {largest}")


number_list = [6, 7, 23, 77]
calculations(number_list)