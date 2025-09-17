# 1. Name:
#      Braeden
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      Receive a list from a file, sort the list, and return it to the user.
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out the best way to automate the test cases was difficult, otherwise
#      The design and test cases made previously made this quite easy.
# 5. How long did it take for you to complete the assignment?
#      1 hour

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

# Sorts an array.
def sort(array):
    size = len(array)
    src = array
    des = [0] * len(array)
    num = 2


    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1

            # Retrieves the first end index.
            while end1 < size and src[end1-1] <= src[end1]:
                end1 += 1

            begin2 = end1

            #checks that there is more in the array to sort.
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            
            # Retrives the second end index
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1

            # Counts the number of loops for sorting subarrays.
            num += 1

            #combines the two found subarrays
            combine(src, des, begin1, begin2, end2)
            begin1 = end2
        
        # Swaps the source and destination arrays.
        src, des = des, src
    return src

# Combines two subarrays together onto another array.
def combine(source, destination, begin1, begin2, end2):
    end1 = begin2

    # Compare the contents of each subarray to each other, and places them in the destination array in order.
    for index in range(begin1, end2):
            if (begin1 < end1) and (begin2 == end2 or source[begin1] < source[begin2]):
                destination[index] = source[begin1]
                begin1 += 1
            else:
                destination[index] = source[begin2]
                begin2 += 1
    return destination

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
    sorted = sort(case)
    print(f"Sorted array: {sorted}\n")