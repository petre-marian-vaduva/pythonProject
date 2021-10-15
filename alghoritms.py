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

# Challenge:
#
# Given a two-dimensional array, return a new array which carries over only those arrays from the original,
# which were not empty and whose items are all of the same type (i.e. homogenous).
# For simplicity, the arrays inside the array will only contain characters and integers.
# Example:
#
# Given [[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]], your function should return [[1, 5, 4], ['b']].
#
# Please keep in mind that for this kata, we assume that empty arrays are not homogenous.
#
# The resultant arrays should be in the order they were originally in and should not have its values changed.

# No implicit type casting is allowed. A subarray [1, '2'] would be considered illegal and should be filtered out.

def filter_homogenous(arrays):
    new_arr = []
    for i in arrays:
        if not i:
            continue
        else:
            is_int = True
            is_str = True
            for j in i:
                if type(j) != int:
                    is_int = False
                elif type(j) != str:
                    is_str = False
            if is_int or is_str:
                new_arr.append(i)
    return new_arr