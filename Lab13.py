# 1. Name:
#      Braeden Pope
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      Take an array from the user and sort it by using a recursive segregation method.
# 4. What was the hardest part? Be as specific as possible.
#      There was a slight bug in the design, but I adjusted the program to resolve it!
# 5. How long did it take for you to complete the assignment?
#      An hour and a half

import json

# Reads the file from a user prompted filenames
def read_file():
    filename = input("What is the name of the file? ")
    try:
        data = open(filename, "r")
        text = data.read()
        array = json.loads(text)
        data.close()

    except FileNotFoundError:
        print("Unable to open file", filename)
    return array

# Starts the sorting process and prints the sorted array.
def sort(array):
    sort_recursive(array, 0, len(array)-1)
    print(f"Sorted Array: {array}\n")

# Checks if the array is sorted, and starts a new sorting round if not.
def sort_recursive(array, i_begin, i_end):
    if (i_end - i_begin < 1 or i_end < 0):
        return
    i_pivot = segregate(array, i_begin, i_end)
    sort_recursive(array, i_begin, i_pivot - 1)
    sort_recursive(array, i_pivot + 1, i_end)

# Segregates the array into two sides and swaps misplaced elements.
def segregate(array, i_begin, i_end):
    if i_begin == i_end:
        return i_begin
    i_pivot = (i_begin + i_end) // 2
    i_up = i_begin
    i_down = i_end

    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            array[i_up], array[i_down] = array[i_down], array[i_up]
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up

# Test Case names.
cases = ["Empty Array", "Singular Array", "Small Sorted Array",
        "Small Unsorted Array", "Sorted Even Array",
        "Reversed Even Array", "Sorted Odd Array", "Reversed Odd Array",
        "Duplicate Array"]

array = read_file()
print()

# Runs through each test case in the file.
for name in cases:
    print(f"Test Case: {name}")
    case = array[name]
    print(f"Original array: {case}")
    sort(case)