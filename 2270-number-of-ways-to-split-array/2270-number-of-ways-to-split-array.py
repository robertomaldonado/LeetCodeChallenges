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
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + sums[-1])
        ans = 0
        for i in range(len(nums)-1):
            left_sum, right_sum = sums[i] , sums[-1] - sums[i]
            ans = ans + 1 if left_sum >= right_sum else ans
        return ans
        