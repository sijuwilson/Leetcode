"""
    Level: Easy
    problem statement:
    Given an array nums containing n distinct numbers in the range \[0, n], return the only number in the range that is missing from the array.

    Example 1:

    Input: nums = \[3,0,1]
    Output: 2
    Explanation:
    n = 3 since there are 3 numbers, so all numbers are in the range \[0,3]. 2 is the missing number in the range since it does not appear in nums.

    Example 2:

    Input: nums = \[0,1]
    Output: 2
    Explanation:
    n = 2 since there are 2 numbers, so all numbers are in the range \[0,2]. 2 is the missing number in the range since it does not appear in nums.

"""
#Approach 1: (Brute force approach)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i
        return -1

#Approach 2: (Optimal approach)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)

"""
    Explanation: 
    we have to find the missing number from 0 - n in the list, So we find the total sum of cosective natural numbers (n\*(n+1))//2 and then we subtract the sum of numbers in the given list.it looks like,
            x+y+z = a (sum of consecutive natural numbers)
            x+z = b (sum of numbers in the given list)
            a-b = (x+y+z) - (x+z) = y (missing number from the given list)

"""