"""
Input: nums = [2,3,1,0]
Output: 2
Approach use sum array: 
[2,  3,  1,  0]
[2,  5,  6,  6]
Iter 1. 
[2 | 5,  6,  6]  .. 2 > 6 - 2 ? 0
Iter 2.
[2,  5 |  6,  6] .. 5 > 6 - 5 ? 1
iter 3.
[2,  5, 6 | 6] ... 6 >= 6-6?  1
count 2
"""
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1
        return ans