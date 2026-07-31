**Level:** Easy
**Problem:**
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

**Example 2:**

Input: nums = [0]
Output: [0]

**Constraints:**

1 <= nums.length <= 104,
-231 <= nums[i] <= 231 - 1.

**Solution:(python3)**

    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            index=-1
            n = len(nums)
            for i in range(n):
                if nums[i]==0:
                    index=i
                    break

            if index == -1:
                return
            
            for j in range (index,n):
                if nums[j]!=0:
                    nums[index]=nums[j]
                    nums[j]=0
                    index+=1
            return