# Given an array of integers, find the sum of its elements.
#
# Input Format
#
# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers representing the array's elements.
#
# Output Format
#
# Print the sum of the array's elements as a single integer.
#
# Sample Input
#
# 6
# 1 2 3 4 10 11

# Sample Output
#
# 31


# Easiest to write
def simpleArraySum(ar):
    return sum(ar)




def simpleArraySumLoop(ar):
    
    sum = 0     # Initialize sum to 0
    for i in ar:    # Start a for-loop that will iterate over each
                    #      element in ar. For each iteration the element
                    #      will be added to sum. The '+=' means 
                    #      sum = sum + i
        sum += i
    return sum
