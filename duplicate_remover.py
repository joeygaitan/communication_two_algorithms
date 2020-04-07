# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

# questions

# assumptions

# my solution

# sudo code 

def dup_remover(arr):
    index = 0

    while (len(arr) - 1 != index):
        print(index, arr, arr[index], arr[index + 1])
        if arr[index] == arr[index + 1]:
            arr.pop(index+1)
        # print(index, arr, arr[index], arr[index + 1])
        index = index + 1


print(dup_remover([1,2,2]))

# print(dup_remover([1,2,2,3,4]))

# if arr[index] == arr[index + 1]:
#     arr.pop(index+1)