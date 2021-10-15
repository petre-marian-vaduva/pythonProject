# Create the function consecutive(arr) that takes an array of integers and
# return the minimum number of integers needed to make the contents of arr consecutive
# from the lowest number to the highest number.
# For example:
# If arr contains [4, 8, 6] then the output should be 2 because
# two numbers need to be added to the array (5 and 7) to make it a
# consecutive array of numbers from 4 to 8. Numbers in arr will be unique.

def consecutive(arr):
    if len(arr) <= 1:
        return 0
    count = 0
    min_num = arr[0]
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    new_arr = []
    for i in range(min_num, max_num+1):
        new_arr.append(i)
    for i in new_arr:
        if i not in arr:
            count += 1
    return count