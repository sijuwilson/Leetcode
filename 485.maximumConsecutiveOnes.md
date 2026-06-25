**Level:** Easy
**Problem:**
Given a binary array nums, return the maximum number of consecutive 1's in the array.

**Example 1:**

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

**Example 2:**

Input: nums = [1,0,1,1,0,1]
Output: 2

**Constraints:**

1 <= nums.length <= 105
nums[i] is either 0 or 1.

**Solution:(python3)**

    class Solution:
        def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            n = len(nums)
            max_ = 0
            i = j = 0
            while i < n:
                if nums[i] == 1:
                    j = i+1
                    while j < n and nums[j] == 1:
                        j += 1
                    max_ = max_ if max_ > j-i else j-i
                    i = j+1
                else : i+=1
            return max_