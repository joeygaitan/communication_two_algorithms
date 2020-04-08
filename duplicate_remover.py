# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Example 1:

# Given nums = [1,1,2],

# [1,2]

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

# It doesn't matter what you leave beyond the returned length.

# questions
# Are there going to be string types?

# assumptions
# its from greatest to smallest
# don't remove the first one

# my solution
# set two variables one to travese through the array. the other to check for duplicates for later both set to zero
# next while loop to check if location is not equal to array length - 1 so it doesn't go out of scope
# then have a conditional that checks if the element is equal to the next. If so delete the next one until the next one isn't equal to the one we started at or location
# else we move location and if location is greater than the length - 1 then return array so we don't go out of scope bro

# sudo code 
# location equal 0
# duplicate_finder equal 0

# while length of array - 1 is not equal to location or index

# if array index or location is equal to array index + 1
#     set duplicate_finder to location + 1
#     remove that array duplicate_finder index element with a pop
# else
#     increment location + 1
    # if location is greater than or equal to lenth of array - 1 then return array 

def dup_remover(arr):
    location = 0
    duplicate_finder = 0

    while (len(arr) - 1 != location):

        # print(arr,location,duplicate_finder,arr[location] == arr[location + 1])

        if arr[location] == arr[location + 1]:
            # print("here")
            duplicate_finder = location + 1
            # print(duplicate_finder)
            arr.pop(duplicate_finder)
        else:
            location += 1
            if location >= len(arr) - 1:
                return arr
        # print(index, arr, arr[index], arr[index + 1])
        
    return arr

print(dup_remover([1,2,2]))

print(dup_remover([1,2,2,3,4]))

print(dup_remover([1,2,3,3,3,3,3]))

print(dup_remover([1,1,1,2,2,3,3,3]))