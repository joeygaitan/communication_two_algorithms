# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Questions
# Are there any duplicates
#what happens if you don't find a match?

# Given
#######
# my work

# assumptions
# there are only numbers in it
# the first match that equals the target is correct
# We find the first two values that equal the target doesn't matter what order it is

## my solution
## we have to loop over each possible pair. I say we can do this linearly
## we have 1 value and search the whole list for a match if not found then we go to the next element and search everything after since everything after it was checked already.
## I'll return false if I cant find it. However, if I do I will return a list of the the two indexs

# sudo code
# i equal to 0
# j equal to 1
# index_list equal to []
# if a[i] + a[j] == target
# if true return index_list.append(i,j)
# while i != array length - 2 # minus two so you don't get a breakout error because you're out of range for the loop
#   for 

def two_sums(array, target):
    i = 0
    j = 1
    

    if array[i] + array[j] == target:
        return [i,j]
    
    i += 1
    j += 1
    
    while (i != len(array) - 1):
        while(j != len(array)):
            # print(i, j,array[i],array[j])
            if array[i] + array[j] == target:
                return [i,j]
            j += 1
        
        i += 1
        j = i + 1
    
    return False

# checks start
print(two_sums([1,2,3],3))
# checks end
print(two_sums([1,2,5,7,10,3,11],14))
# checks middle
print(two_sums([1,4,5,7,5],12))