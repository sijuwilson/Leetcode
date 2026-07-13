"""
    Level: Medium
    Problem:
    Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.

    Example 2:

    Input: target = 4, nums = [1,4,4]
    Output: 1

    Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target: return 0
        mn = len(nums)+1
        cs = 0
        i = 0 
        for j in range(len(nums)):
            cs+=nums[j]
            while cs >= target:
                mn = min(mn,(j-i)+1)
                cs -= nums[i]
                i+=1
        return mn